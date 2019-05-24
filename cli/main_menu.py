from cli.ops_menu import ops_menu
from cli.open_file_menu import open_file_menu
from cli.select_automata_menu import print_selected
from cli.message import show_error
from cli.save_automaton import save_select_automaton
from cli.close_automata_menu import close_automata_menu
from cli.vis_automaton import vis_automaton
from cli.display_menu import display_menu
from time import sleep


menu_msg = '''
DESwiz Main Menu
-------------------------------------------------------------------
Type one of the below commands
-------------------------------------------------------------------
o: open a file for an automaton
l: list all automata
b: begin to perform operations
s: save an automaton
c: close automata
v: visualize an automaton
e: exit
'''


def main_menu(next_screens, automata):
    display_menu(menu_msg)

    inpt = input().lower()
    if inpt in ["o", "open"]:
        open_file_menu(automata)
    elif inpt in ["l", "list"]:
        print_selected(automata)
        sleep(0.2)
    elif inpt in ["b", "begin"]:
        ops_menu(automata)
    elif inpt in ["s", "save"]:
        save_select_automaton(automata)
    elif inpt in ["c", "close"]:
        close_automata_menu(automata)
    elif inpt in ["v", "visualize"]:
        vis_automaton(automata)
    elif inpt in ["e", "exit"]:
        print("Exiting...")
        next_screens.pop()  # Remove main menu from the stack
    else:
        show_error("Command not recognized")