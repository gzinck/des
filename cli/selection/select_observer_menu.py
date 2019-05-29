from cli.display.message import show_error, show_notification
from cli.display.display_menu import display_menu


# Part 1 of the message describing what the menu is for
menu_msg = '''
Select Observer Menu
-------------------------------------------------------------------
Type the index of your desired observer, from 0 to '''

# Part 2 of the message describing what the menu is for
menu_msg_2 = ''' inclusive:
0 is the system controller
'''

# Part 3 of the message describing what the menu is for
menu_msg_3 = '''
-------------------------------------------------------------------
#: select the index
e: exit without saving
'''


def select_observer_menu(automaton):
    """Allows the user to select which observer to use for an operation (each
    observer has an observable alphabet, a controllable alphabet, and a set of
    secret states).

    Parameters
    ----------
    automaton : dict

    Returns
    -------
    int
        The index of the observer which has been selected
    """
    num_obs = len(automaton["events"]["observable"])
    max_input = str(num_obs - 1)

    # Create the menu message
    msg = menu_msg + max_input + menu_msg_2
    if num_obs > 1:
        msg += "1 through " + max_input + " are agents"
    msg += menu_msg_3

    # Display the message
    display_menu(msg)

    while True:
        inpt = input()
        try:
            # If we get a good number, select it!
            if int(inpt) in range(num_obs):
                show_notification("Selected:\n" + inpt)
                return int(inpt)
            else:
                show_error("Not a valid observer index")
        except ValueError:
            # Check if the user wishes to quit
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None
            else:
                show_error("Command not recognized")
