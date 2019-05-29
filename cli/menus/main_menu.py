from cli.menus.ops_menu import ops_menu
from cli.menus.open_file_menu import open_file_menu
from cli.selection.select_automata_menu import print_selected
from cli.display.message import show_error
from cli.menus.close_automata_menu import close_automata_menu
from cli.save_and_visualize import select_and_save_temp, select_and_save
from cli.display.display_menu import display_menu
from time import sleep


# The message describing what the menu is for
menu_msg = '''
DESwiz Main Menu
-------------------------------------------------------------------
Type one of the below commands
-------------------------------------------------------------------
o: open a file for an automaton
l: list all automata
b: begin to perform operations
s: save automata
c: close automata
v: visualize an automaton
e: exit
'''


def main_menu(next_screens, automata, temp_dir):
    """Main menu for the application with all of the actions that are possible
    in the application at a high level.

    Parameters
    ----------
    next_screens : list
        The next screens that will be shown (a stack). This is not used much
        with the current version of the application, but it might be used in
        the future
    automata : list
        List of all automata loaded into the program
    temp_dir : str
        The string representing the temporary directory for files

    Returns
    -------
    None
    """
    display_menu(menu_msg)

    # Based on input, choose which type of operation to perform
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