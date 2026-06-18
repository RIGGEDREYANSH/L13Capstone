import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Hello, World!")
        self.label.pack(pady=20)

        self.entry = tk.Entry(self, width=30)
        self.entry.pack(pady=10)
        self.entry.insert(0, "Type here...")

        self.button = tk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

        self.output_label = tk.Label(self, text="Output will appear here.")
        self.output_label.pack(pady=10)

    def on_button_click(self):
        self.button.config(text="Clicked!")
        self.output_label.config(text=self.entry.get())

if __name__ == "__main__":
    app = Application()
    app.mainloop() 