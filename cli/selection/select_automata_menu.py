from cli.display.message import show_error, show_notification
from cli.display.display_menu import display_menu


def print_selected(automata, selected=None):
    if selected is None:
        selected = [False] * len(automata)
    msg = "All Automata:\n----------------------------------\n"
    for i in range(len(automata)):
        if selected[i]:
            msg += str(i) + " " + automata[i]["name"] + " " + "SELECTED"
        else:
            msg += str(i) + " " + automata[i]["name"]
        if i != len(automata) - 1:
            msg += "\n"
    show_notification(msg)


multiple_menu_msg = '''
-------------------------------------------------------------------
Type the index of your desired automaton to add/remove it
#: select the index
s: exits and selects automata
e: exit and cancels selection
'''


def select_automata_menu(automata, min_selection=1, menu_name=None):
    if menu_name is None:
        menu_name = "Select Multiple Automata Menu"
    else:
        menu_name = "Select Automata for " + menu_name
    display_menu(menu_name + multiple_menu_msg)
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
            elif inpt in ["s", "save"]:
                result = [automata[i] for i in range(num_options) if selected[i]]
                if len(result) >= min_selection:
                    sel = [item["name"] for item in result]
                    show_notification("Selected:\n" + str(sel))
                    return result
                else:
                    show_error("At least " + str(min_selection)
                               + " automata must be selected")
            else:
                show_error("Command not recognized")


single_menu_msg = '''
-------------------------------------------------------------------
Type the index of your desired automaton to add/remove it
#: select the index
e: exit without saving
'''


def select_automaton_menu(automata, menu_name=None):
    if menu_name is None:
        menu_name = "Select Single Automaton Menu"
    else:
        menu_name = "Select Automaton for " + menu_name
    display_menu(menu_name + single_menu_msg)
    num_options = len(automata)
    selected = [False] * num_options

    while True:
        print_selected(automata, selected)
        inpt = input()
        try:
            if int(inpt) in range(num_options):
                show_notification("Selected:\n" +
                                  str(automata[int(inpt)]["name"]))
                return automata[int(inpt)]
            else:
                show_error("Index not valid, max index is "
                           + str(num_options - 1))
        except ValueError:
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None
            else:
                show_error("Command not recognized")
