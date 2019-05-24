from cli.menus.main_menu import main_menu
from tempfile import TemporaryDirectory

# import tkinter as tk
#
# root = tk.Tk()
# root.withdraw()
# root.lift()

# Maintain a stack for the screens shown (this avoids lots of recursion)
screens = [main_menu]
automata = []
with TemporaryDirectory() as temp_dir:
    while len(screens) > 0:
        next_screen = screens[-1]
        next_screen(screens, automata, temp_dir)