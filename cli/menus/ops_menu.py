from basic_ops.determinize import determinize
from basic_ops.opacity import check_opacity
from basic_ops.product import product
from basic_ops.union import union
from basic_ops.accessible import get_accessible
from basic_ops.controllable import get_controllable
from basic_ops.coaccessible import get_coaccessible
from basic_ops.leakage_automaton import create_leakage_automaton
from arenas.construct_arena import construct_arena
from arenas.construct_attractor import construct_attractor
from modular_opacity.modular_opacity_verification import check_modular_opacity
from communication.construct_communication_arena import construct_communication_arena

from cli.selection.select_automata_menu import select_automata_menu, select_automaton_menu
from cli.selection.select_observer_menu import select_observer_menu
from cli.selection.select_secret_menu import select_secret_menu
from cli.menus.name_automaton_menu import name_automaton_menu
from cli.display.message import show_error, show_notification
from cli.display.display_menu import display_menu
from cli.save_and_visualize import save_temp
from cli.menus.select_heuristic import select_heuristic


# The message describing what the menu is for
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
ca: coaccessible (prune off states that do not reach marked states)
l: create leakage automaton with respect to an agent's perspective
   and another agent's secret
e: exit to main menu
-------------------------------------------------------------------
Leaking Secrets (2019 paper) ops
-------------------------------------------------------------------
ba: build arena
bt: build attractor (adds bad states to the arena)
bp: build pruned arena (removes bad states using controllable)
-------------------------------------------------------------------
Enforcing Opacity in Modular Systems (2019 paper) ops
-------------------------------------------------------------------
om: check current state opacity for a modular system
-------------------------------------------------------------------
Arenas for Communication with Multiple Agents ops
-------------------------------------------------------------------
bca: build communication arena from (Ricker, 2013)
'''


def __save(automata, automaton, temp_dir):
    """Helper method that saves an automaton into the automata list by naming
    it and appending it to the list. It also visualizes the automaton in the
    temp folder.

    Parameters
    ----------
    automata : list
        The list of open automata
    automaton : dict
        The automaton that is open
    temp_dir : str
        The directory containing the temp files (i.e., images and graphviz dot)

    Returns
    -------
    None
    """
    name_automaton_menu(automata, automaton)
    automata.append(automaton)
    save_temp(automaton, temp_dir)


def ops_menu(automata, temp_dir):
    """Opens a menu with options for different operations that can be performed.

    Parameters
    ----------
    automata : list
        The list of automata currently open in the program
    temp_dir : str
        The temporary directory for the session

    Returns
    -------
    None
    """
    display_menu(menu_msg)

    inpt = input().lower()

    # Choose which operation to perform
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
        selected = select_automaton_menu(automata, "Controllability Operation")
        if selected is not None:
            result = get_controllable(selected)
            __save(automata, result, temp_dir)
    elif inpt in ["ca", "coaccessible"]:
        selected = select_automaton_menu(automata, "Coaccessibility Operation")
        if selected is not None:
            result = get_coaccessible(selected)
            __save(automata, result, temp_dir)
    elif inpt in ["l", "leakage"]:
        selected = select_automaton_menu(automata, "Get Leakage Automaton")
        if selected is not None:
            observer = select_observer_menu(selected)
            if observer is not None:
                secret = select_secret_menu(selected)
                if secret is not None:
                    result = create_leakage_automaton(selected, observer, secret)
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
    elif inpt in ["om"]:
        show_notification("With this operation, we assume the\nattacker can see all items in the\nshared alphabet,as per Enforcing\nOpacity in Modular Systems (2020)")
        selected = select_automata_menu(automata, 1, "Checking Opacity for Modular Systems")
        if selected is not None:
            heuristic = select_heuristic()
            result = check_modular_opacity(selected, heuristic = heuristic)
            show_notification("The modular system is " + ("opaque" if result else "not opaque"))
    elif inpt in ["bca"]:
        selected = select_automaton_menu(automata, "Constructing Communication Arena")
        if selected is not None:
            result = construct_communication_arena(selected)
            __save(automata, result, temp_dir)
    elif inpt in ["e", "exit"]:
        pass
    else:
        show_error("Command not recognized")
