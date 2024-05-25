import tkinter as tk

# create the GUI window
window = tk.Tk()
window.geometry("800x600")

# create the title label
title_label = tk.Label(window, text="Build Your Own Story", font=("Arial", 25))
title_label.pack(pady=30)

# create the input fields for the story elements
name_label = tk.Label(window, text="Enter a name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack(pady=20)

place_label = tk.Label(window, text="Enter a place:")
place_label.pack()
place_entry = tk.Entry(window)
place_entry.pack(pady=20)

verb_label = tk.Label(window, text="Enter a verb:")
verb_label.pack()
verb_entry = tk.Entry(window)
verb_entry.pack(pady=20)

noun_label = tk.Label(window, text="Enter a noun:")
noun_label.pack()
noun_entry = tk.Entry(window)
noun_entry.pack(pady=20)

# create the function to build the story
def build_story():
    name = name_entry.get(font=("Arial",20)
    place = place_entry.get()
    verb = verb_entry.get()
    noun = noun_entry.get()

    story = f"{name} went to {place} and {verb} a {noun}."

    story_label.configure(text=story)

# create the button to build the story
build_button = tk.Button(window, text="Build Story", command=build_story)
build_button.pack(pady=20)

# create the label to display the story
story_label = tk.Label(window, font=("Arial", 25))
story_label.pack()

# start the GUI
window.mainloop()
