from tkinter import filedialog
import tkinter as tk
from json import load, JSONDecodeError

from structure_validation.automaton_validator import validate
from cli.menus.name_automaton_menu import name_automaton_menu
from cli.display.message import show_error, show_notification
from cli.display.display_menu import display_menu
from cli.save_and_visualize import save_temp


# The message describing what the menu is for
menu_msg = '''
Open File Menu
-------------------------------------------------------------------
In the popup window, find the JSON file representing your automaton
and select open to import it into the application
'''


def open_file_menu(automata, temp_dir):
    """Opens a file using a file dialog box and immediately visualizes it if it
    is a valid automaton.

    Parameters
    ----------
    automata : list
        List of currently open automata
    temp_dir : str
        The temp directory for placing images

    Returns
    -------
    None
    """
    display_menu(menu_msg)

    # Open the file dialog box
    root = tk.Tk()
    root.withdraw()
    root.lift()
    file_path = filedialog.askopenfilename()

    # Validate that a file was selected
    if len(file_path) == 0:
        show_error("No file selected")
    else:
        curr = None

        # Attempt to load the file's JSON
        with open(file_path) as f:
            try:
                curr = load(f)
            except JSONDecodeError:
                show_error("Failed to read JSON")
                return

        # Attempt to validate the automaton
        try:
            validate(curr)
        except Exception as e:
            show_error("Automaton validation failure: " + str(e))
            return

        # Add the automaton
        name_automaton_menu(automata, curr)
        automata.append(curr)
        save_temp(curr, temp_dir)
