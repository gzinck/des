from cli.selection.select_automata_menu import print_selected
from cli.display.message import show_error, show_notification
from cli.save_and_visualize import save
from cli.display.display_menu import display_menu


# The message describing what the menu is for
menu_msg = '''
Close Automata Menu
-------------------------------------------------------------------
Type one of the below commands
-------------------------------------------------------------------
Select all automata you wish to close
#: selects the automaton index #
e: exit without closing the selected automata
c: close the selected automata without saving
s: save the selected automata and close them
'''


def close_automata_menu(automata):
    """Menu for closing automaton. It has three major tasks: 1) selecting the
    automata, then 2) closing without saving or 3) closing with saving.
    When an automaton has been "closed", it is no longer in the automata list.
    If it has also been saved, the json and pdf are saved to disk.

    Parameters
    ----------
    automata : list
        List of all automata which are available to choose

    Returns
    -------
    None
    """
    display_menu(menu_msg)

    num_options = len(automata)
    selected = [False] * num_options

    # Keep on selecting automata to close until choose to stop
    while True:

        # Print what we've selected so far
        print_selected(automata, selected)
        inpt = input()
        try:
            # If input is fine, toggle the selection
            if int(inpt) in range(num_options):
                inpt = int(inpt)
                selected[inpt] = not selected[inpt]
        except ValueError:
            # Else, see if we want to exit, close, or save
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None # Exit without closing
            elif inpt in ["c", "close"]:

                # Close all automata selected
                result = [automata[i] for i in range(num_options) if
                          selected[i]]
                for item in result:
                    automata.remove(item)
                sel = [item["name"] for item in result]
                show_notification("The following were closed:\n" + str(sel))
                return
            elif inpt in ["s", "save"]:

                # Save all automata selected and close all those not failed
                result = [automata[i] for i in range(num_options) if
                          selected[i]]

                # Keep track of those that fail to save, and don't close them
                failed = []
                for item in result:
                    saved = save(item)
                    if saved:
                        automata.remove(item)
                    else:
                        show_error("Could not save, so automaton not closed")
                        failed.append(item)

                # Show which ones were actually closed
                sel = [item["name"] for item in result if item not in failed]
                show_notification("The following were saved and closed:\n" + str(sel))
            else:
                show_error("Command not recognized")

