from cli.message import show_error, show_notification


def print_selected(automata, selected=None):
    if selected is None:
        selected = [False] * len(automata)
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(len(automata)):
        if selected[i]:
            print(i, automata[i]["name"], "SELECTED")
        print(i, automata[i]["name"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()


def select_automata_menu(automata):
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Select Multiple Automata Menu")
    print("-------------------------------------------------------------------")
    print("Type the index of your desired automaton to add/remove it")
    print("#: select the index")
    print("e: exit without saving")
    print("s: exits with saving")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    num_options = len(automata)
    selected = [False] * num_options

    while True:
        print_selected(automata, selected)
        inpt = input()
        try:
            while int(inpt) in range(num_options):
                selected[inpt] = not selected[inpt]
                print_selected(automata, selected)
                inpt = input()
        except ValueError:
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None
            elif input in ["s", "save"]:
                result = [automata[i] for i in range(num_options) if selected[i]]
                if len(result) > 1:
                    sel = [item["name"] for item in result]
                    show_notification("Selected:\n" + str(sel))
                    return result
                else:
                    show_error("At least two automata must be selected")
            else:
                show_error("Command not recognized")


def select_automaton_menu(automata):
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Select Single Automaton Menu")
    print("-------------------------------------------------------------------")
    print("Type the index of your desired automaton")
    print("#: select the index")
    print("e: exit without saving")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
        except ValueError:
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None
            else:
                show_error("Command not recognized")