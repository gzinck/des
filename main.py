from cli.main_menu import main_menu

import tkinter as tk

root = tk.Tk()
root.withdraw()

# Maintain a stack for the screens shown (this avoids lots of recursion)
screens = [main_menu]
automata = []
while len(screens) > 0:
    next_screen = screens[-1]
    next_screen(screens, automata)