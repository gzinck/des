from basic_ops.determinize import determinize
from basic_ops.opacity import check_opacity
from basic_ops.product import product
from basic_ops.union import union
from basic_ops.accessible import get_accessible
from basic_ops.controllable import get_controllable
from arenas.construct_arena import construct_arena
from arenas.construct_attractor import construct_attractor

from cli.select_automata_menu import select_automata_menu, select_automaton_menu
from cli.select_observer_menu import select_observer_menu
from cli.name_automaton_menu import name_automaton_menu
from cli.message import show_error, show_notification
from cli.display_menu import display_menu


menu_msg = '''
Operations Menu
-------------------------------------------------------------------
Type one of the below commands
Then, the operation will be performed on the current automaton
-------------------------------------------------------------------
d: determinization
o: check current state opacity
u: union (parallel composition)
p: product (intersection)
a: accessible (prune off states not accessible from initial)
c: controllable (get the supremal controllable wrt bad states)
e: exit to main menu
-------------------------------------------------------------------
Leaking Secrets (2019 paper) ops
-------------------------------------------------------------------
ba: build arena
bt: build attractor (adds bad states to the arena)
bp: build pruned arena (removes bad states using controllable)
'''


def ops_menu(automata):
    display_menu(menu_msg)

    inpt = input().lower()
    if inpt in ["d", "determinization"]:
        selected = select_automaton_menu(automata)
        if selected is not None:
            observer = select_observer_menu(selected)
            if observer is not None:
                result = determinize(selected, observer)
                name_automaton_menu(automata, result)
                automata.append(result)
    elif inpt in ["o", "opacity"]:
        selected = select_automaton_menu(automata)
        if selected is not None:
            observer = select_observer_menu(selected)
            if observer is not None:
                result = check_opacity(selected, observer)
                print("With respect to the observer " + str(observer) +
                      ", the system is opaque")
                print("for the following secrets:")
                print([i for i, x in enumerate(result) if x is True])
                print("The system is not opaque for the following secrets:")
                print([i for i, x in enumerate(result) if x is False])
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
    elif inpt in ["a", "accessible"]:
        selected = select_automaton_menu(automata)
        if selected is not None:
            result = get_accessible(selected)
            name_automaton_menu(automata, result)
            automata.append(result)
    elif inpt in ["c", "controllable"]:
        selected = select_automaton_menu(automata)
        if selected is not None:
            result = get_controllable(selected)
            name_automaton_menu(automata, result)
            automata.append(result)
    elif inpt in ["ba"]:
        selected = select_automaton_menu(automata)
        if selected is not None:
            result = construct_arena(selected)
            name_automaton_menu(automata, result)
            automata.append(result)
            show_notification("Bad states:\n" + str(result["states"]["bad"]))
    elif inpt in ["bt"]:
        selected = select_automaton_menu(automata)
        if selected is not None:
            result = construct_attractor(selected)
            name_automaton_menu(automata, result)
            automata.append(result)
            show_notification("Bad states:\n" + str(result["states"]["bad"]))
    elif inpt in ["bp"]:
        selected = select_automaton_menu(automata)
        if selected is not None:
            result = get_controllable(construct_attractor(selected))
            name_automaton_menu(automata, result)
            automata.append(result)
    elif inpt in ["e", "exit"]:
        pass
    else:
        show_error("Command not recognized")