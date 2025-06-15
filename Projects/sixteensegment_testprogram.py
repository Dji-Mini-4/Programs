def sixteen_segment_display(text):
    """
    Translates alphabetical and numeral characters into a sixteen-segment display.
    :param text: The input string to be displayed.
    :return: A string representation of the sixteen-segment display.
    """
    # Define the sixteen-segment display patterns for supported characters
    segments = {
        'A': ["  ███  ", " █   █ ", " █████ ", " █   █ ", " █   █ "],
        'B': [" ████  ", " █   █ ", " ████  ", " █   █ ", " ████  "],
        'C': ["  ███  ", " █   █ ", " █     ", " █   █ ", "  ███  "],
        'D': [" ███   ", " █  █  ", " █   █ ", " █  █  ", " ███   "],
        'E': [" █████ ", " █     ", " ███   ", " █     ", " █████ "],
        'F': [" █████ ", " █     ", " ███   ", " █     ", " █     "],
        'G': ["  ███  ", " █     ", " █  ██ ", " █   █ ", "  ███  "],
        'H': [" █   █ ", " █   █ ", " █████ ", " █   █ ", " █   █ "],
        'I': ["  ███  ", "   █   ", "   █   ", "   █   ", "  ███  "],
        'J': ["   ███ ", "    █  ", "    █  ", " █  █  ", "  ██   "],
        'K': [" █   █ ", " █  █  ", " ███   ", " █  █  ", " █   █ "],
        'L': [" █     ", " █     ", " █     ", " █     ", " █████ "],
        'M': [" █   █ ", " ██ ██ ", " █ █ █ ", " █   █ ", " █   █ "],
        'N': [" █   █ ", " ██  █ ", " █ █ █ ", " █  ██ ", " █   █ "],
        'O': ["  ███  ", " █   █ ", " █   █ ", " █   █ ", "  ███  "],
        'P': [" ████  ", " █   █ ", " ████  ", " █     ", " █     "],
        'Q': ["  ███  ", " █   █ ", " █   █ ", " █  ██ ", "  ████ "],
        'R': [" ████  ", " █   █ ", " ████  ", " █  █  ", " █   █ "],
        'S': ["  ███  ", " █     ", "  ███  ", "     █ ", "  ███  "],
        'T': [" █████ ", "   █   ", "   █   ", "   █   ", "   █   "],
        'U': [" █   █ ", " █   █ ", " █   █ ", " █   █ ", "  ███  "],
        'V': [" █   █ ", " █   █ ", " █   █ ", "  █ █  ", "   █   "],
        'W': [" █   █ ", " █   █ ", " █ █ █ ", " ██ ██ ", " █   █ "],
        'X': [" █   █ ", "  █ █  ", "   █   ", "  █ █  ", " █   █ "],
        'Y': [" █   █ ", "  █ █  ", "   █   ", "   █   ", "   █   "],
        'Z': [" █████ ", "    █  ", "   █   ", "  █    ", " █████ "],
        '0': ["  ███  ", " █   █ ", " █   █ ", " █   █ ", "  ███  "],
        '1': ["   █   ", "  ██   ", "   █   ", "   █   ", "  ███  "],
        '2': ["  ███  ", "     █ ", "  ███  ", " █     ", " █████ "],
        '3': ["  ███  ", "     █ ", "  ███  ", "     █ ", "  ███  "],
        '4': [" █   █ ", " █   █ ", " █████ ", "     █ ", "     █ "],
        '5': [" █████ ", " █     ", "  ███  ", "     █ ", "  ███  "],
        '6': ["  ███  ", " █     ", " ████  ", " █   █ ", "  ███  "],
        '7': [" █████ ", "     █ ", "    █  ", "   █   ", "   █   "],
        '8': ["  ███  ", " █   █ ", "  ███  ", " █   █ ", "  ███  "],
        '9': ["  ███  ", " █   █ ", "  ███  ", "     █ ", "  ███  "],
        ' ': ["       ", "       ", "       ", "       ", "       "],
    }

    # Convert the input text to uppercase
    text = text.upper()

    # Build the sixteen-segment display output
    output = [""] * 5
    for char in text:
        if char in segments:
            for i in range(5):
                output[i] += segments[char][i] + "  "
        else:
            for i in range(5):
                output[i] += "       " + "  "  # Add blank space for unsupported characters

    # Join the rows and return the result
    return "\n".join(output)


# Example usage (if run directly)
if __name__ == "__main__":
    sample_text = "HELLO 123"
    print(sixteen_segment_display(sample_text))