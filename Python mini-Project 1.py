#Story Generator
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Story Generator")

# Create the Listbox widget to display the story titles
story_titles = ["Thirsty Crow", "Fox and Crane", "Suspense"]
listbox = tk.Listbox(root)
for title in story_titles:
    listbox.insert(tk.END, title)
listbox.pack()

# Create a button to select a story title
def select_title():
    # Get the index of the selected story title
    index = listbox.curselection()[0]
    selected_title = story_titles[index]

    # Create a new window for the input of words
    input_window = tk.Toplevel(root)
    input_window.title("Enter Words")

    # Create entry fields for each part of speech
    if selected_title == "Thirsty Crow":

        container_label = tk.Label(input_window, text="Enter a container :")
        container_label.pack()
        container_entry = tk.Entry(input_window)
        container_entry.pack()

        adverb_label = tk.Label(input_window, text="Enter an adverb:")
        adverb_label.pack()
        adverb_entry = tk.Entry(input_window)
        adverb_entry.pack()

    elif selected_title == "Fox and Crane":
        adjective_label = tk.Label(input_window, text="Enter an adjective:")
        adjective_label.pack()
        adjective_entry = tk.Entry(input_window)
        adjective_entry.pack()

        container_label = tk.Label(input_window, text="Enter a container:")
        container_label.pack()
        container_entry = tk.Entry(input_window)
        container_entry.pack()

    elif selected_title == "Suspense":
        noun_label = tk.Label(input_window, text="Enter a noun:")
        noun_label.pack()
        noun_entry = tk.Entry(input_window)
        noun_entry.pack()

        verb_label = tk.Label(input_window, text="Enter a verb:")
        verb_label.pack()
        verb_entry = tk.Entry(input_window)
        verb_entry.pack()

        adverb_label = tk.Label(input_window, text="Enter a adverb:")
        adverb_label.pack()
        adverb_entry = tk.Entry(input_window)
        adverb_entry.pack()

        adjective_label = tk.Label(input_window, text="Enter an adjective:")
        adjective_label.pack()
        adjective_entry = tk.Entry(input_window)
        adjective_entry.pack()

    # Create a button to generate the story
    def generate_story():
        # Get the input values
        '''noun = noun_entry.get()
        adjective = adjective_entry.get()
        container = container_entry.get()
        adverb = adverb_entry.get()
        verb = verb_entry.get()
        '''
        # Create entry fields for each part of speech
        if selected_title == "Thirsty Crow":
            container = container_entry.get()
            adverb = adverb_entry.get()

            # Generate the story
            story = f"{selected_title} is a story about a thirsty crow who finds a {container} with just a little bit of water at the bottom. The crow can't reach the water, but then he has an idea. He starts dropping small stones into the {container} one by one. The water level starts rising, and soon the crow can drink from it {adverb}."
            messagebox.showinfo("Generated Story", story)

        elif selected_title == "Fox and Crane":
            container = container_entry.get()
            adjective = adjective_entry.get()

            # Generate the story
            story = f"{selected_title} is a story about a {adjective} fox who invites a crane for dinner. The fox serves soup in a flat {container}, so he can easily slurp it up with his tongue. But the crane couldn't drink the soup because of it's long beak. Then the crane invited the fox over to its house and offered food in a jug with long-narrow neck. The fox feels embarrassed and realizes that he had been repaid for his behaviour with the crane."
            messagebox.showinfo("Generated Story", story)
        elif selected_title == "Suspense":
            noun = noun_entry.get()
            verb = verb_entry.get()
            adverb = adverb_entry.get()
            adjective = adjective_entry.get()

            # Generate the story
            story = f"{selected_title} is a {adjective} story about a {noun} who decides to {verb} {adverb}."
            messagebox.showinfo("Generated Story", story)
        # Close the input window
        input_window.destroy()

    generate_button = tk.Button(
        input_window, text="Generate Story", command=generate_story
    )
    generate_button.pack()


generate_button = tk.Button(root, text="Select Story", command=select_title)
generate_button.pack()

# Run the main loop
root.mainloop()
