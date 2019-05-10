from tkinter import filedialog
from json import load, JSONDecodeError

from structure_validation.automaton_validator import validate
from cli.name_automaton_menu import name_automaton_menu
from cli.message import show_error


def open_file_menu(automata):
    print("\n")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("Open File Menu")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print()
    file_path = filedialog.askopenfilename()
    print(file_path)
    if len(file_path) == 0:
        show_error("No file selected")
    else:
        curr = None
        with open(file_path) as f:
            try:
                curr = load(f)
            except JSONDecodeError:
                show_error("Failed to read JSON")
                return
        try:
            validate(curr)
        except Exception as e:
            show_error("Automaton validation failure: " + str(e))
            return
        print("Added automaton")
        name_automaton_menu(automata, curr)
        automata.append(curr)