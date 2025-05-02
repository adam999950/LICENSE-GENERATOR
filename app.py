import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import datetime
import os

# Function to generate the license
def generate_license():
    license_type = license_var.get()  # Get selected license type
    author = author_entry.get()  # Get author name
    year = datetime.datetime.now().year  # Get current year

    try:
        # Read the template for the selected license
        with open(f'licenses/{license_type}.txt', 'r', encoding='utf-8') as file:
            template = file.read()
            license_text = template.replace('[YEAR]', str(year)).replace('[AUTHOR]', author)
            output_text.delete('1.0', tk.END)  # Clear previous text
            output_text.insert(tk.END, license_text)  # Insert generated license
    except FileNotFoundError:
        messagebox.showerror('Error', f'License template {license_type}.txt not found.')

# Function to save the generated license to a file
def save_license():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(output_text.get('1.0', tk.END))  # Write generated text to file
        messagebox.showinfo('Success', f'License saved as {file_path}')

# GUI setup
root = tk.Tk()
root.title('Open-Source License Generator')
root.geometry('600x500')

# License selection
license_label = tk.Label(root, text='Select License:')
license_label.pack()

license_var = tk.StringVar(value='mit')  # Default to MIT license
license_dropdown = ttk.Combobox(root, textvariable=license_var, values=['mit', 'gpl', 'apache'])
license_dropdown.pack()

# Author name input
author_label = tk.Label(root, text='Author / Organization:')
author_label.pack()

author_entry = tk.Entry(root, width=40)
author_entry.pack()

# Generate button
generate_button = tk.Button(root, text='Generate License', command=generate_license)
generate_button.pack(pady=10)

# License output area
output_text = tk.Text(root, wrap='word', height=15, width=70)
output_text.pack()

# Save button
save_button = tk.Button(root, text='Save to file', command=save_license)
save_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
