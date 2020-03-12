from cli.display.message import show_error, show_notification
from cli.display.display_menu import display_menu


# Message describing what the menu is for
menu_msg = '''
-------------------------------------------------------------------
Select a delta for taus in the system.
A delta value is the number of events between clock ticks.
-------------------------------------------------------------------
#: select the delta value
e: exit without saving
'''


def select_delta_menu():
    """Allows the user to select a delta value to use.

    Returns
    -------
    int
        The index of the observer which has been selected
    """

    # Display the message
    display_menu(menu_msg)

    while True:
        inpt = input()
        try:
            # If we get a good number, select it!
            int(inpt)
            show_notification("Selected:\n" + inpt)
            return int(inpt)
        except ValueError:
            # Check if the user wishes to quit
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None
            else:
                show_error("Command not recognized")
