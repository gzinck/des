from basic_ops.determinize import determinize
from basic_ops.product import product
from basic_ops.union import union
from arenas.construct_arena import construct_arena

from cli.select_automata_menu import select_automata_menu, select_automaton_menu
from cli.name_automaton_menu import name_automaton_menu
from cli.message import show_error, show_notification


def ops_menu(automata):
    print("\n")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("Operations Menu")
    print("-------------------------------------------------------------------")
    print("Type one of the below commands")
    print("Then, the operation will be performed on the current automaton")
    print("-------------------------------------------------------------------")
    print("d: determinization")
    print("u: union (parallel composition)")
    print("p: product (intersection)")
    print("e: exit to main menu")
    print("-------------------------------------------------------------------")
    print("Leaking Secrets (2019 paper) ops")
    print("-------------------------------------------------------------------")
    print("a: construct arena")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print()

    inpt = input().lower()
    if inpt in ["d", "determinization"]:
        selected = select_automaton_menu(automata)
        if selected is not None:
            result = determinize(selected)
            name_automaton_menu(automata, result)
            automata.append(result)
    elif inpt in ["u", "union", "parallel composition"]:
        selected = select_automata_menu(automata)
        if selected is not None:
            result = union(selected)
            name_automaton_menu(automata, result)
            automata.append(result)
    elif inpt in ["p", "product", "intersection"]:
        selected = select_automata_menu(automata)
        if selected is not None:
            result = product(selected)
            name_automaton_menu(automata, result)
            automata.append(result)
    elif inpt in ["a", "arena"]:
        selected = select_automaton_menu(automata)
        if selected is not None:
            result = construct_arena(selected)
            name_automaton_menu(automata, result)
            automata.append(result)
            show_notification("Bad states:\n" + str(result["states"]["bad"]))
    elif inpt in ["e", "exit"]:
        pass
    else:
        show_error("Command not recognized")