from cli.menus.main_menu import main_menu
from tempfile import TemporaryDirectory

"""
This main file runs the DES application on the command line.
"""

# Maintain a stack for the screens shown (this avoids lots of recursion)
screens = [main_menu]
automata = []

# Opens up a temp directory which is used in the application
with TemporaryDirectory() as temp_dir:
    while len(screens) > 0:
        next_screen = screens[-1]
        next_screen(screens, automata, temp_dir)