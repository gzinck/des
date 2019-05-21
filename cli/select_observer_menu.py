from cli.message import show_error, show_notification


def select_observer_menu(automaton):
    num_obs = len(automaton["events"]["observable"])
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Select Observer Menu")
    print("-------------------------------------------------------------------")
    print("Type the index of your desired observer, from 0 to "
          + str(num_obs - 1) + " inclusive")
    print("#: select the index")
    print("e: exit without saving")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        inpt = input()
        try:
            if int(inpt) in range(num_obs):
                show_notification("Selected:\n" + inpt)
                return int(inpt)
            else:
                show_error("Not a valid observer index")
        except ValueError:
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None
            else:
                show_error("Command not recognized")