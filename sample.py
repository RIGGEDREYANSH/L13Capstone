import tkinter as tk
from tkinter import ttk, messagebox

def show_info():
    # Classic dialog box - old feature
    messagebox.showinfo("Hello", "Welcome to Tkinter!")

def update_progress():
    # Modern progress bar update - new/ttk feature
    progress['value'] += 20
    if progress['value'] >= 100:
        progress['value'] = 0

# --- MAIN WINDOW ---
root = tk.Tk()
root.title("Tkinter Old & New Features")
root.geometry("450x300")

# --- MODERN FEATURES (ttk) ---
# Create a Notebook (tabbed pane)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Tab 1: Progress & Buttons
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Main Tools")

# ttk widgets use the native OS look
ttk.Label(tab1, text="Modern Progress Tracker:").pack(pady=5)
progress = ttk.Progressbar(tab1, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=5)

ttk.Button(tab1, text="Step Progress", command=update_progress).pack(pady=5)
ttk.Button(tab1, text="Show Message", command=show_info).pack(pady=5)

# Tab 2: Classic Features
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Legacy Widgets")

# --- CLASSIC FEATURES ---
# Classic Tkinter Button and Entry Box (without ttk styling)
label_legacy = tk.Label(tab2, text="Classic Label (Tk)", bg="lightgray", fg="black")
label_legacy.pack(pady=5, fill="x")

# Classic Text Entry
entry_legacy = tk.Entry(tab2, width=30)
entry_legacy.insert(0, "Type legacy text here...")
entry_legacy.pack(pady=5)

def read_legacy():
    # Accessing text in a classic Entry widget
    user_text = entry_legacy.get()
    label_legacy.config(text=f"You typed: {user_text}")

# Classic Button
button_legacy = tk.Button(tab2, text="Update Legacy Label", command=read_legacy, bg="blue", fg="white")
button_legacy.pack(pady=5)

# Run the application
root.mainloop()