from basic_ops.determinize import determinize
from basic_ops.opacity import check_opacity
from basic_ops.product import product
from basic_ops.union import union
from basic_ops.accessible import get_accessible
from basic_ops.controllable import get_controllable
from arenas.construct_arena import construct_arena
from arenas.construct_attractor import construct_attractor

from cli.selection.select_automata_menu import select_automata_menu, select_automaton_menu
from cli.selection.select_observer_menu import select_observer_menu
from cli.menus.name_automaton_menu import name_automaton_menu
from cli.display.message import show_error, show_notification
from cli.display.display_menu import display_menu
from cli.save_and_visualize import save_temp


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


def __save(automata, automaton, temp_dir):
    name_automaton_menu(automata, automaton)
    automata.append(automaton)
    save_temp(automaton, temp_dir)


def ops_menu(automata, temp_dir):
    display_menu(menu_msg)

    inpt = input().lower()
    if inpt in ["d", "determinization"]:
        selected = select_automaton_menu(automata, "Determinization")
        if selected is not None:
            observer = select_observer_menu(selected)
            if observer is not None:
                result = determinize(selected, observer)
                __save(automata, result, temp_dir)
    elif inpt in ["o", "opacity"]:
        selected = select_automaton_menu(automata, "Checking Opacity")
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
        selected = select_automata_menu(automata, 2, "Parallel Composition")
        if selected is not None:
            result = union(selected)
            __save(automata, result, temp_dir)
    elif inpt in ["p", "product", "intersection"]:
        selected = select_automata_menu(automata, 2, "Intersection")
        if selected is not None:
            result = product(selected)
            __save(automata, result, temp_dir)
    elif inpt in ["a", "accessible"]:
        selected = select_automaton_menu(automata, "Accessibility Operation")
        if selected is not None:
            result = get_accessible(selected)
            __save(automata, result, temp_dir)
    elif inpt in ["c", "controllable"]:
        selected = select_automaton_menu(automata, "Controllable Operation")
        if selected is not None:
            result = get_controllable(selected)
            __save(automata, result, temp_dir)
    elif inpt in ["ba"]:
        selected = select_automaton_menu(automata, "Constructing Arena")
        if selected is not None:
            result = construct_arena(selected)
            __save(automata, result, temp_dir)
            show_notification("Bad states:\n" + str(result["states"]["bad"]))
    elif inpt in ["bt"]:
        selected = select_automaton_menu(automata, "Constructing Attractor")
        if selected is not None:
            result = construct_attractor(selected)
            __save(automata, result, temp_dir)
            show_notification("Bad states:\n" + str(result["states"]["bad"]))
    elif inpt in ["bp"]:
        selected = select_automaton_menu(automata, "Pruning Arena")
        if selected is not None:
            result = get_controllable(construct_attractor(selected))
            __save(automata, result, temp_dir)
    elif inpt in ["e", "exit"]:
        pass
    else:
        show_error("Command not recognized")