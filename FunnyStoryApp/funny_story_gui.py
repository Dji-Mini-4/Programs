import tkinter as tk
from tkinter import messagebox, PhotoImage
import random
import re
import os
import pygame
import time
from PIL import Image, ImageTk

POEM_TEMPLATES = [
    "There once was a {adj} {noun},\nWho wore a ridiculous crown.\nIt tried to {verb} in the rain,\nBut slipped and screamed '{silly_word}' in pain.",
    
    "Roses are {color},\nViolets are {color},\nMy {noun} exploded,\nBecause it tried to {verb} harder.",
    
    "The {adj} {animal} did a dance,\nWearing only glitter pants.\nIt {verb}ed across the yard,\nThen ate a {noun}, extra charred.",
    
    "I had a {adj} little dream,\nWhere {plural_noun} made me scream.\nThey {verb}ed around in jelly beans,\nThen flew away in flying jeans.",
    
    "A {adj} {creature} in the snow,\nTried to {verb} but stubbed its toe.\nIt yelled '{silly_word}' and ran away,\nStraight into a chocolate buffet.",
    
    "Twinkle twinkle, {adj} star,\nWhy'd you park your {noun} so far?\nI tried to {verb} and reach your light,\nBut fell into a bowl of Sprite."
]


TEMPLATES = [
    'The {adj} {noun} {verb} {adv} over the {adj} {noun}.',
    'Once upon a time, a {adj} {noun} decided to {verb} on a {adj} {noun}.',
    'Aliens invaded my {place} and started {verb}ing all the {plural_noun}.',
    'Why are there {plural_noun} inside my {noun}? Must be {adj} magic.',
    'A {adj} banana tried to {verb} my {body_part}!',
    'Breaking news: {plural_noun} have taken over {place} by {verb}ing.',
    'My dream job? A {adj} {job} who feeds {plural_noun} to dragons.',
    'The {adj} {creature} {verb}ed across the {adj} {place}, singing "{silly_word}!"',
    'I accidentally {verb}ed my {relative} with a {adj} {object}.',
    'Every {time}, I {verb} a {adj} {noun} and hope it doesn’t bite me.',
    'The {adj} vending machine gave me a {adj} {object} instead of chips.',
    'In {place}, they celebrate {event} by {verb}ing {plural_noun}.',
    'A {adj} {animal} challenged me to a {event} in the middle of {place}.',
    'My {adj} neighbor keeps {verb}ing on my {body_part}.',
    'To impress the {job}, I wore a {adj} {object} and juggled {plural_noun}.',
    'Beware of the {adj} {creature} that {verb}s when you say "{silly_word}".',
    'I opened the fridge and found a {adj} {animal} eating {plural_noun}.',
    'The haunted {place} was full of {adj} {plural_noun} whispering "{silly_word}".',
    'On my last trip to {place}, I {verb}ed a {adj} {noun} with my {body_part}.',
    'Legend says if you {verb} in front of a mirror and say "{silly_word}", a {adj} {noun} appears.',
    'I tried to {verb} but slipped on a {adj} {object} and landed in {place}.',
    'The science fair winner made a {adj} machine that {verb}s {plural_noun}.',
    'My phone autocorrected "Hi" to "{silly_word}", and now I’m married to a {adj} {animal}.',
    'The {adj} clown juggled {plural_noun} while {verb}ing on a {object}.',
    'I have a {adj} fear of {plural_noun} after a {event} at {place}.',
    'Never trust a {adj} {job} who offers you {plural_noun} during a thunderstorm.',
    'Aliens turned my {object} into a {adj} {animal} named "{silly_word}".',
    'My {relative} says you should always {verb} before petting a {adj} {animal}.',
    'There’s a {adj} conspiracy involving {plural_noun}, {job}s, and {place}.',
    'I spilled {food} on my {body_part}, and now a {adj} {creature} lives there.',
    'They kicked me out of {place} for trying to {verb} the {plural_noun}.',
    'Why did the {noun} {verb} the {animal}? Because it was {adj}!',
    'I woke up next to a {adj} {creature} whispering "{silly_word}" into my {body_part}.',
    'During the {event}, a {adj} {noun} danced with a {adj} {job}.',
    'My talking {animal} keeps telling me to {verb} the {plural_noun}.',
    'The cursed {object} turns into a {adj} {animal} when you {verb} it.',
    'I just invented a {adj} {object} that can {verb} through {place}.',
    'A {adj} {relative} appeared in my dream and screamed "{silly_word}!"',
    'Every full moon, I turn into a {adj} {creature} that only {verb}s {plural_noun}.',
    'At the zoo, I saw a {adj} {animal} {verb}ing with a {object}.',
    'My {adj} alarm clock keeps shouting "{silly_word}" at 3 a.m.'
]

ALL_TEMPLATES = TEMPLATES + POEM_TEMPLATES

def extract_placeholders(template):
    return re.findall(r'{(.*?)}', template)

def play_funny_sound(volume_percent):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("funny.wav")
        pygame.mixer.music.set_volume(volume_percent / 100.0)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Sound error: {e}")

class FunnyStoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("😂 Funny Story Generator 😂")
        self.root.geometry("480x600")

        self.template = random.choice(TEMPLATES)
        self.placeholders = extract_placeholders(self.template)
        self.entries = {}
        self.story_frame = None

        self.volume = tk.IntVar(value=30)
        self.laugh_count = 0
        self.laugh_counter_var = tk.StringVar(value="Laughs: 0")
        self.last_laugh_times = []
        self.too_funny_shown = False
        self.laugh_emojis = ["😂", "🤣", "😹", "😆"]
        self.emoji_index = 0

        self.laugh_btn = None

        self.set_background("laugh_tile.png")
        self.build_form()

    def set_background(self, tile_path):
        try:
            tile = Image.open(tile_path).resize((64, 64), Image.ANTIALIAS).convert("RGBA")

            # Fade the emoji
            faded_tile = Image.new("RGBA", tile.size)
            for x in range(tile.width):
                for y in range(tile.height):
                    r, g, b, a = tile.getpixel((x, y))
                    faded_tile.putpixel((x, y), (r, g, b, int(a * 0.1)))  # 10% opacity

            # Make a tall scrollable canvas
            self.bg_canvas_img = Image.new("RGBA", (480, 1200))
            for x in range(0, 480, faded_tile.width):
                for y in range(0, 1200, faded_tile.height):
                    self.bg_canvas_img.paste(faded_tile, (x, y), faded_tile)

            self.bg_offset = 0
            self.bg_image = ImageTk.PhotoImage(self.bg_canvas_img.crop((0, 0, 480, 600)))
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            self.animate_background()
        except Exception as e:
            print(f"Animated background error: {e}")

    def animate_background(self):
        self.bg_offset = (self.bg_offset + 1) % 600
        cropped = self.bg_canvas_img.crop((0, self.bg_offset, 480, self.bg_offset + 600))
        self.bg_image = ImageTk.PhotoImage(cropped)
        self.bg_label.config(image=self.bg_image)
        self.bg_label.image = self.bg_image
        self.root.after(50, self.animate_background)

    def build_form(self):
        tk.Label(self.root, text="Fill the blanks to generate your story:", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)
        form_frame = tk.Frame(self.root, bg="#ffffff")
        form_frame.pack(pady=5)

        for ph in self.placeholders:
            if ph not in self.entries:
                label = ph.replace('_', ' ').capitalize()
                row = tk.Frame(form_frame, bg="#ffffff")
                row.pack(fill="x", padx=10, pady=2)
                tk.Label(row, text=f"{label}:", width=15, anchor="w", bg="#ffffff").pack(side="left")
                entry = tk.Entry(row, width=30)
                entry.pack(side="left")
                self.entries[ph] = entry

        bottom_row = tk.Frame(self.root, bg="#ffffff")
        bottom_row.pack(pady=10)
        tk.Label(bottom_row, text="Volume:", bg="#ffffff").pack(side="left")
        tk.Scale(bottom_row, from_=0, to=100, orient=tk.HORIZONTAL, variable=self.volume, length=120).pack(side="left", padx=5)
        tk.Button(bottom_row, text="✨ Create Story ✨", command=self.make_story, bg="#ffdd57", font=("Arial", 10, "bold")).pack(side="left", padx=10)

    def make_story(self):
        inputs = {}
        for ph, entry in self.entries.items():
            val = entry.get().strip()
            if not val:
                messagebox.showerror("Missing Input", f"Please enter a value for '{ph}'.")
                return
            inputs[ph] = val

        story = self.template.format(**inputs)
        self.display_story(story)

    def display_story(self, story):
        if self.story_frame:
            self.story_frame.destroy()
        self.story_frame = tk.Frame(self.root, bg="#ffffff")
        self.story_frame.pack(pady=10)

        tk.Label(self.story_frame, text="Here's your funny story!", font=("Arial", 12, "bold"), bg="#ffffff").pack()
        tk.Message(self.story_frame, text=story, width=400, font=("Arial", 10), bg="#fffff0").pack(pady=5)

        try:
            img = PhotoImage(file="funny.png")
            tk.Label(self.story_frame, image=img, bg="#ffffff").pack()
            self.story_frame.image = img
        except Exception as e:
            print(f"No image found: {e}")

        laugh_frame = tk.Frame(self.story_frame, bg="#ffffff")
        laugh_frame.pack(pady=5)

        self.laugh_btn = tk.Button(laugh_frame, text="😂 Laugh", command=self.laugh_clicked, bg="#b3f7ff", font=("Arial", 10, "bold"))
        self.laugh_btn.pack(side="left", padx=5)
        tk.Label(laugh_frame, textvariable=self.laugh_counter_var, font=("Arial", 9), bg="#ffffff").pack(side="left")

        tk.Button(self.story_frame, text="📃 Save Story", command=lambda: self.save_story(story), bg="#afe8a0", font=("Arial", 10)).pack(pady=5)

    def laugh_clicked(self):
        self.laugh_count += 1
        self.laugh_counter_var.set(f"Laughs: {self.laugh_count}")
        play_funny_sound(self.volume.get())

        emoji = self.laugh_emojis[self.emoji_index % len(self.laugh_emojis)]
        self.laugh_btn.config(text=f"{emoji} Laugh")
        self.emoji_index += 1

        current = time.time()
        self.last_laugh_times = [t for t in self.last_laugh_times if current - t < 2.0]
        self.last_laugh_times.append(current)

        if len(self.last_laugh_times) >= 4:
            self.shake_window()

        if self.laugh_count >= 10 and not self.too_funny_shown:
            self.too_funny_shown = True
            messagebox.showinfo("TOO FUNNY!", "🤣 You’ve laughed 10 times! Take a breath!")

    def shake_window(self):
        original_x = self.root.winfo_x()
        original_y = self.root.winfo_y()

        for _ in range(10):
            dx = random.randint(-10, 10)
            dy = random.randint(-10, 10)
            self.root.geometry(f"+{original_x + dx}+{original_y + dy}")
            self.root.update()
            time.sleep(0.03)

        self.root.geometry(f"+{original_x}+{original_y}")

    def save_story(self, story):
        filename = "stories.txt"
        first_time = not os.path.exists(filename)
        with open(filename, "a", encoding="utf-8") as f:
            if first_time:
                f.write("=== Funny Stories Archive ===\n")
            f.write(story + "\n\n")
        messagebox.showinfo("Saved", f"Your story was saved to '{filename}'!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FunnyStoryApp(root)
    root.mainloop()