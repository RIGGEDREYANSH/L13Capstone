import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Hello, World!")
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.config(text="Button clicked!")
        self.button.config(text="Clicked!")

if __name__ == "__main__":
    app = Application()
    app.mainloop() 