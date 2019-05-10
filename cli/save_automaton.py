from cli.select_automata_menu import select_automaton_menu
from cli.message import show_error, show_notification
from tkinter import filedialog
from json import dump


def save_automaton(automata):
    automaton = select_automaton_menu(automata)
    if automaton is None:
        return
    location = filedialog.asksaveasfilename(
        title="Automaton Export Filename",
        defaultextension="txt"
    )
    if len(location) == 0:
        show_error("No location given")
    else:
        with open(location, 'w') as f:  # writing JSON object
            dump(automaton, f, sort_keys=True, indent=4)
            show_notification("Saved to " + location)
