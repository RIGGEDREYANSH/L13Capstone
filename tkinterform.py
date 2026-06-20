import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Form")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Enter your name:")
        self.label.pack(pady=10)

        self.Entry = tk.Entry(self)
        self.Entry.pack(pady=10)

        self.label = tk.Label(self, text="Enter your age:")
        self.label.pack(pady=10)

        self.Entry = tk.Entry(self)
        self.Entry.pack(pady=10)

        self.label = tk.Label(self, text="Enter your address:")
        self.label.pack(pady=10)

        self.Entry = tk.Entry(self)
        self.Entry.pack(pady=10)

        self.button = tk.Button(self, text="Submit")
        self.button.pack(pady=10)

        self.output_label = tk.Label(self, text="")
        self.output_label.pack(pady=10)

        self.button.config(command=self.on_button_click)

    def on_button_click(self):
            name = self.Entry.get()
            age = self.Entry.get()
            address = self.Entry.get()
            self.output_label.config(text=f"Name: {name}, Age: {age}, Address: {address}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()