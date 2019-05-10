from time import sleep


def name_automaton_menu(automata, automaton):
    bad_names = set([a["name"] for a in automata])
    bad_names.add("")
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Name Your Automaton")
    print("-------------------------------------------------------------------")
    print("Give your automaton a name and press enter")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    name = input()
    while name in bad_names:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        sleep(0.2)
        print("Name already taken! Try again")
        sleep(0.2)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        sleep(0.2)
        name = input()
    automaton["name"] = name
