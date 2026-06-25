import tkinter as tk

def add_item():
    item = item_entry.get()
    quantity = qty_entry.get()
    listbox.insert(tk.END, f"{item} - {quantity}")
    item_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)

def delete_item():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

root = tk.Tk()
root.title("Grocery List")
root.geometry("400x300")

tk.Label(root, text="Item Name").pack()
item_entry = tk.Entry(root)
item_entry.pack()

tk.Label(root, text="Quantity").pack()
qty_entry = tk.Entry(root)
qty_entry.pack()

tk.Button(root, text="Add Item", command=add_item).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

tk.Button(root, text="Delete Item", command=delete_item).pack()

root.mainloop()
