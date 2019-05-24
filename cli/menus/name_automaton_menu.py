from cli.display.display_menu import display_menu
from cli.display.message import show_error, show_notification


menu_msg = '''
Name Your Automaton
-------------------------------------------------------------------
Give your automaton a name and press enter
'''


def name_automaton_menu(automata, automaton):
    bad_names = set([a["name"] for a in automata])
    bad_names.add("")
    if "name" in automaton:
        if automaton["name"] not in bad_names:
            show_notification("Imported automaton " + automaton["name"])
            return

    display_menu(menu_msg)
    name = input()
    while name in bad_names:
        show_error("Name already taken! Try again")
        name = input()
    automaton["name"] = name
    show_notification("Imported automaton " + automaton["name"])
