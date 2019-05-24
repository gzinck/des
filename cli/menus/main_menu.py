from cli.menus.ops_menu import ops_menu
from cli.menus.open_file_menu import open_file_menu
from cli.selection.select_automata_menu import print_selected
from cli.display.message import show_error
from cli.menus.close_automata_menu import close_automata_menu
from cli.save_and_visualize import select_and_save_temp, select_and_save
from cli.display.display_menu import display_menu
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


def main_menu(next_screens, automata, temp_dir):
    display_menu(menu_msg)

    inpt = input().lower()
    if inpt in ["o", "open"]:
        open_file_menu(automata, temp_dir)
    elif inpt in ["l", "list"]:
        print_selected(automata)
        sleep(0.2)
    elif inpt in ["b", "begin"]:
        ops_menu(automata, temp_dir)
    elif inpt in ["s", "save"]:
        select_and_save(automata)
    elif inpt in ["c", "close"]:
        close_automata_menu(automata)
    elif inpt in ["v", "visualize"]:
        select_and_save_temp(automata, temp_dir)
    elif inpt in ["e", "exit"]:
        print("Exiting...")
        next_screens.pop()  # Remove main menu from the stack
    else:
        show_error("Command not recognized")