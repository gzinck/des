import os
from tkinter import filedialog
from json import dump
from graph_viz.visualize import visualize
from cli.selection.select_automata_menu import select_automata_menu
from cli.display.message import show_error, show_notification


def save_temp(automaton, temp_dir):
    """Saves an automaton to the temporary directory provided and opens it in a
    PDF viewer.

    Parameters
    ----------
    automaton : dict
        The automaton to save in the temp directory (and visualize)
    temp_dir : str
        Path to the temporary directory

    Returns
    -------
    None
    """
    index = 0
    path = temp_dir + "/" + automaton["name"] + str(index)
    while os.path.isfile(path):
        index += 1
        path = temp_dir + "/" + automaton["name"] + str(index)
    with open(path + ".json", 'w') as f:  # writing JSON object
        dump(automaton, f, sort_keys=True, indent=4)
    visualize(automaton, path)


def select_and_save_temp(automata, temp_dir):
    selected = select_automata_menu(automata)
    if selected is not None:
        for a in selected:
            save_temp(a, temp_dir)


def save(automaton):
    show_notification("Select a location to save " + automaton["name"])
    location = filedialog.asksaveasfilename(
        title="Automaton Export Filename",
        defaultextension="json"
    )
    if len(location) == 0:
        show_error("No location given")
        return False
    else:
        with open(location, 'w') as f:  # writing JSON object
            dump(automaton, f, sort_keys=True, indent=4)

        location = location[:-5]
        visualize(automaton, location)
        show_notification("Saved to " + location)
        return True


def select_and_save(automata):
    selected = select_automata_menu(automata)
    if selected is not None:
        for a in selected:
            save(a)
