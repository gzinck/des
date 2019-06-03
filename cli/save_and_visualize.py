import os
from tkinter import filedialog
from json import dump
from graph_viz.visualize import visualize
from cli.selection.select_automata_menu import select_automata_menu
from cli.display.message import show_error, show_notification
import global_settings


def save_temp(automaton, temp_dir, must_show=False):
    """Saves an automaton to the temporary directory provided and opens it in a
    PDF viewer.
    If the user has turned off auto-vis, then nothing happens here.

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
    auto_vis = global_settings.settings["graphviz_auto_vis"]
    if auto_vis or must_show:
        index = 0
        path = temp_dir + "/" + automaton["name"] + str(index)
        while os.path.isfile(path):
            index += 1
            path = temp_dir + "/" + automaton["name"] + str(index)
        with open(path + ".json", 'w') as f:  # writing JSON object
            dump(automaton, f, sort_keys=True, indent=4)
        visualize(automaton, path)


def select_and_save_temp(automata, temp_dir):
    """Allows a user to select an automaton to save/visualize. After selection,
    if the selection was valid, it saves and visualizes the automaton.

    Parameters
    ----------
    automata : list
        All automata available for selection
    temp_dir : str
        Path of the temporary folder for saving temp files

    Returns
    -------
    None
    """
    menu_name = "Select Multiple Automata for Visualization"
    selected = select_automata_menu(automata, menu_name=menu_name)
    if selected is not None:
        for a in selected:
            save_temp(a, temp_dir, must_show=True)


def save(automaton):
    """Saves an automaton to a user-defined location in JSON form, dot form, and
    the GraphViz PDF form.

    Parameters
    ----------
    automaton : dict
        The automaton to save

    Returns
    -------
    None
    """
    show_notification("Select a location to save " + automaton["name"])
    location = filedialog.asksaveasfilename(
        title="Automaton Export Filename",
        defaultextension="json"
    )
    # If selected a location, save it
    if len(location) == 0:
        show_error("No location given")
        return False
    else:
        with open(location, 'w') as f:  # writing JSON object
            dump(automaton, f, sort_keys=True, indent=4)

        # Remove the .json extension
        location = location[:-5]
        visualize(automaton, location, view=False)
        show_notification("Saved to " + location)
        return True


def select_and_save(automata):
    """Allows the user to select an automaton and then subsequently choose where
    to save it.

    Parameters
    ----------
    automata : list
        The list of automata that can be saved

    Returns
    -------
    None
    """
    selected = select_automata_menu(automata)
    if selected is not None:
        for a in selected:
            save(a)
