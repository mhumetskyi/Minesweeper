import tkinter as tk


class MainMenu(tk.Menu):
    def __init__(self):
        super().__init__()

        levels_menu = tk.Menu(self, tearoff=0)
        levels_menu.add_command(label="Легко")
        levels_menu.add_command(label="Нормально")
        levels_menu.add_command(label="Складно")

        game_menu = tk.Menu(self, tearoff=0)
        game_menu.add_cascade(label="Складність", menu=levels_menu)
        game_menu.add_command(label="Вихід", command=quit)

        self.add_cascade(label="Гра", menu=game_menu)

    def quit(self):
        self.destroy()
