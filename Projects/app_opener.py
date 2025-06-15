import sys

# Handle pip-required modules with try/except and error messages
try:
    import difflib
    import time
    import shutil
    import os
    from math import ceil
except ImportError as e:
    print(f"Required standard library module missing: {e.name}")
    sys.exit(1)

try:
    from windows_tools.installed_software import get_installed_software
except ImportError:
    print("Missing required module: windows_tools. Install it with 'pip install windows_tools.installed_software'.")
    sys.exit(1)

try:
    import AppOpener
except ImportError:
    print("Missing required module: AppOpener. Install it with 'pip install AppOpener'.")
    sys.exit(1)

try:
    import pygetwindow as gw
except ImportError:
    gw = None
    print("Optional module 'pygetwindow' not found. App window detection will be disabled.")


def wait_for_window(title_keyword, timeout=15):
    if not gw:
        return
    print(f"Waiting for '{title_keyword}' window to appear...")
    start = time.time()
    while time.time() - start < timeout:
        windows = gw.getAllTitles()
        if any(title_keyword.lower() in w.lower() for w in windows):
            print(f"Window '{title_keyword}' detected. Exiting.")
            return
        time.sleep(0.5)
    print("Window did not appear in time.")

print('App Opener, by Jayden')
print('This program lets you open an installed application on your computer!\n')

# Get installed software (returns a list of dicts)
apps = get_installed_software()

# Build a list of unique display names and their install locations (if available)
app_names = []
app_paths = []
seen = set()
for app in apps:
    name = app.get('name')
    if name and name not in seen:
        seen.add(name)
        app_names.append(name)
        path = app.get('install_location') or app.get('uninstall_string')
        app_paths.append(path)

# Sort app names for easier reading
app_names_sorted = sorted(app_names)
app_paths_sorted = [app_paths[app_names.index(name)] for name in app_names_sorted]

# Print available apps as a numbered list, auto-fit per line, and only truncate if necessary
print('Available apps:\n')
try:
    term_width = shutil.get_terminal_size().columns
except Exception:
    term_width = 80  # fallback

# Find the max app name length for spacing, but don't truncate unless needed
max_app_len = max(len(app) for app in app_names_sorted) if app_names_sorted else 10
sep = '  |  '
# Reserve space for the number and separator
num_width = len(str(len(app_names_sorted))) + 2  # e.g., "12. "
col_width = num_width + max_app_len + len(sep)
apps_per_line = max(1, term_width // col_width)

# Calculate how many rows are needed
total = len(app_names_sorted)
rows = ceil(total / apps_per_line)

for row in range(rows):
    entries = []
    for col in range(apps_per_line):
        idx = row * apps_per_line + col
        if idx >= total:
            break
        app = app_names_sorted[idx]
        # Only truncate if the app name is too long for the terminal
        display_app = app
        max_name_len = term_width // apps_per_line - num_width - len(sep)
        if len(display_app) > max_name_len:
            display_app = display_app[:max(0, max_name_len - 3)] + '...' if max_name_len > 3 else display_app[:max_name_len]
        entry = f"{str(idx+1).rjust(num_width-2)}. {display_app.ljust(max_name_len)}"
        entries.append(entry)
    print(sep.join(entries))
print()  # Final newline

print('\nEnter the app name (copy-paste or type, case-insensitive):')
while True:
    app_name_input = input('> ').strip()
    if not app_name_input:
        print('That\'s not valid.')
        continue
    # Case-insensitive match
    matches = [name for name in app_names if name.lower() == app_name_input.lower()]
    if matches:
        idx = app_names.index(matches[0])
        app_path = app_paths[idx]
        if not app_path:
            print("Warning: No executable path found for this app. Will try AppOpener as fallback.")
        break
    # Fuzzy match suggestion (case-insensitive)
    lower_app_names = [name.lower() for name in app_names]
    close_matches = difflib.get_close_matches(app_name_input.lower(), lower_app_names, n=1, cutoff=0.6)
    if close_matches:
        suggestion_lower = close_matches[0]
        idx = lower_app_names.index(suggestion_lower)
        suggestion = app_names[idx]
        app_path = app_paths[idx]
        yn = input(f"Did you mean '{suggestion}'? (y/n): ").strip().lower()
        if yn == 'y':
            if not app_path:
                print("Warning: No executable path found for this app. Will try AppOpener as fallback.")
            break
    print('That\'s not valid.')
    continue

input(f'Ready? Press Enter to open {app_names[idx]}...')

# Try os.startfile first, then AppOpener.open as fallback
opened = False
try:
    if app_path:
        os.startfile(app_path)
        opened = True
except Exception as e:
    print(f"os.startfile() failed: {e}")

if not opened:
    try:
        AppOpener.open(app_names[idx], output=False)
        opened = True
    except Exception as e:
        print(f"AppOpener.open() failed: {e}")
        opened = False

# Only wait for window if something was actually launched
if opened and gw:
    wait_for_window(app_names[idx])