from cli.select_automata_menu import print_selected
from cli.message import show_error, show_notification
from cli.save_automaton import save_automaton
from cli.display_menu import display_menu


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

    display_menu(menu_msg)

    num_options = len(automata)
    selected = [False] * num_options

    while True:
        print_selected(automata, selected)
        inpt = input()
        try:
            while int(inpt) in range(num_options):
                inpt = int(inpt)
                selected[inpt] = not selected[inpt]
                print_selected(automata, selected)
                inpt = input()
        except ValueError:
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None
            elif inpt in ["c", "close"]:
                result = [automata[i] for i in range(num_options) if
                          selected[i]]
                for item in result:
                    automata.remove(item)
                sel = [item["name"] for item in result]
                show_notification("The following were closed:\n" + str(sel))
                return
            elif inpt in ["s", "save"]:
                result = [automata[i] for i in range(num_options) if
                          selected[i]]
                failed = []
                for item in result:
                    show_notification("Select a location to save " + item["name"])
                    saved = save_automaton(item)
                    if saved:
                        automata.remove(item)
                    else:
                        show_error("Could not save, so automaton not closed")
                        failed.append(item)
                sel = [item["name"] for item in result if item not in failed]
                show_notification("The following were saved and closed:\n" + str(sel))
                return
            else:
                show_error("Command not recognized")

