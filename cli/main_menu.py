from cli.ops_menu import ops_menu
from cli.open_file_menu import open_file_menu
from cli.select_automata_menu import print_selected
from cli.message import show_error
from cli.save_automaton import save_automaton
from time import sleep


def main_menu(next_screens, automata):
    print()
    print("###################################################################")
    print("DESwiz Main Menu")
    print("-------------------------------------------------------------------")
    print("Type one of the below commands")
    print("-------------------------------------------------------------------")
    print("o: open a file for an automaton")
    print("l: list all automata")
    print("b: begin to perform operations")
    print("s: save an automaton")
    print("e: exit")
    print("###################################################################")
    print()

    inpt = input().lower()
    if inpt in ["o", "open"]:
        open_file_menu(automata)
    elif inpt in ["l", "list"]:
        print_selected(automata)
        sleep(0.2)
    elif inpt in ["b", "begin"]:
        ops_menu(automata)
    elif inpt in ["s", "save"]:
        save_automaton(automata)
    elif inpt in ["e", "exit"]:
        print("Exiting...")
        next_screens.pop()  # Remove main menu from the stack
    else:
        show_error("Command not recognized")