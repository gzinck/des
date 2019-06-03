from cli.display.message import show_error, show_notification
from cli.display.display_menu import display_menu


def print_selected(automata, selected=None):
    """Helper method that prints all of the automata's names and indicates if
    they have been selected, based on the booleans given.

    Parameters
    ----------
    automata : list
        List of automata to print
    selected : list
        List of booleans indicating that the index was selected (if None, then
        assumes that none are selected)

    Returns
    -------
    None
    """
    if selected is None:
        selected = [False] * len(automata)

    # Construct the message to send to the user
    msg = "All Automata:\n----------------------------------\n"
    for i in range(len(automata)):
        if selected[i]:
            msg += str(i) + " " + automata[i]["name"] + " " + "SELECTED"
        else:
            msg += str(i) + " " + automata[i]["name"]
        if i != len(automata) - 1:
            msg += "\n"

    if selected is not None:
        msg += "\n"
        msg += "Continue to select automata, or type s to finish"
    # Show the message to the user
    show_notification(msg)


# The message describing what the menu is for
multiple_menu_msg = '''
-------------------------------------------------------------------
Type the index of your desired automaton to add/remove it
#: select the index
s: exits and selects automata
e: exit and cancels selection
'''


def select_automata_menu(automata, min_selection=1, menu_name=None):
    """Menu for selecting multiple automata.

    Parameters
    ----------
    automata : list
        All automata that are available for selection
    min_selection : int
        The minimum number of automata needed
    menu_name : str
        The name for the menu

    Returns
    -------
    lst
        The automata that have been selected (or None if none selected)
    """
    if menu_name is None:
        menu_name = "Select Multiple Automata Menu"
    else:
        menu_name = "Select Automata for " + menu_name

    # Show the menu
    display_menu(menu_name + multiple_menu_msg)
    num_options = len(automata)
    selected = [False] * num_options

    # Keep selecting until type "e" or "exit"
    while True:
        print_selected(automata, selected)
        inpt = input()
        try:
            # Get the integer input from the user and select it
            if int(inpt) in range(num_options):
                inpt = int(inpt)
                selected[inpt] = not selected[inpt]
        except ValueError:
            # Check if we are done
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None
            elif inpt in ["s", "save"]:
                result = [automata[i] for i in range(num_options) if selected[i]]
                if len(result) >= min_selection:
                    sel = [item["name"] for item in result]
                    show_notification("Selected:\n" + str(sel))
                    return result
                else:
                    # Prevent exit because selection was inadequate
                    show_error("At least " + str(min_selection)
                               + " automata must be selected")
            else:
                show_error("Command not recognized")


# The message describing what the menu is for
single_menu_msg = '''
-------------------------------------------------------------------
Type the index of your desired automaton to add/remove it
#: select the index
e: exit without saving
'''


def select_automaton_menu(automata, menu_name=None):
    """Menu for selecting a single automaton.

    Parameters
    ----------
    automata : list
        All automata that are available for selection
    menu_name : str
        The name for the menu

    Returns
    -------
    dict
        The automaton selected (or None if none selected)
    """
    if menu_name is None:
        menu_name = "Select Single Automaton Menu"
    else:
        menu_name = "Select Automaton for " + menu_name

    # Display the menu
    display_menu(menu_name + single_menu_msg)
    num_options = len(automata)
    selected = [False] * num_options

    # Keep selecting until type "e" or "exit"
    while True:
        print_selected(automata, selected)
        inpt = input()
        try:
            # If successfully selected, return the selection
            if int(inpt) in range(num_options):
                show_notification("Selected:\n" +
                                  str(automata[int(inpt)]["name"]))
                return automata[int(inpt)]
            else:
                show_error("Index not valid, max index is "
                           + str(num_options - 1))
        except ValueError:
            # See if the user wanted to exit
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None
            else:
                show_error("Command not recognized")
