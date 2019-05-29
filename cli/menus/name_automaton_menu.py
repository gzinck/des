from cli.display.display_menu import display_menu
from cli.display.message import show_error, show_notification


# The message describing what the menu is for
menu_msg = '''
Name Your Automaton
-------------------------------------------------------------------
Give your automaton a name and press enter
'''


def name_automaton_menu(automata, automaton):
    """Gives the user the opportunity to name an automaton, if the automaton
    is currently unnamed (or has a name that conflicts with another automaton
    already loaded).

    Parameters
    ----------
    automata : list
        The automata that are currently open (excluding the current automaton)
    automaton : dict
        The automaton to name (not in the list parameter)

    Returns
    -------
    None
    """
    bad_names = set([a["name"] for a in automata])
    bad_names.add("")

    # Checks if automaton already has a valid name; if so, done
    if "name" in automaton:
        if automaton["name"] not in bad_names:
            show_notification("Imported automaton " + automaton["name"])
            return

    # Otherwise, shows a menu to request a name
    display_menu(menu_msg)
    name = input()
    while name in bad_names:
        show_error("Name already taken! Try again")
        name = input()

    # Name the automaton and notify the user
    automaton["name"] = name
    show_notification("Imported automaton " + automaton["name"])
