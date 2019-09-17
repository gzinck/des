from modular_opacity.heuristics import no_heuristic, most_shared_heuristic, least_new_heuristic

from cli.display.message import show_error, show_notification
from cli.display.display_menu import display_menu

menu_msg = '''
Select Heuristic Menu
-------------------------------------------------------------------
Pick the heuristic you want to use when combining automata in the
modular system. All of them will be theoretically correct, but some
heuristics may be faster.
-------------------------------------------------------------------
0 No heuristic
1 Most shared events
2 Least new events
'''
def select_heuristic():
    """Opens a menu to select a heuristic for composing systems in a modular
    architecture to speed up operations.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    display_menu(menu_msg)

    inpt = input()
    while(True):
        if inpt in ["0"]:
            show_notification("Selected no heuristic")
            return no_heuristic
        elif inpt in ["1"]:
            show_notification("Selected most shared events")
            return most_shared_heuristic
        elif inpt in ["2"]:
            show_notification("Selected least new events")
            return least_new_heuristic
        else:
            show_error("Command not recognized")
            inpt = input()
