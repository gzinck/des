from cli.display.message import show_error, show_notification
from cli.display.display_menu import display_menu


menu_msg = '''
Select Observer Menu
-------------------------------------------------------------------
Type the index of your desired observer, from 0 to '''

menu_msg_2 = ''' inclusive:
0 is the system controller
Subsequent indices are agents
-------------------------------------------------------------------
#: select the index
e: exit without saving
'''


def select_observer_menu(automaton):
    num_obs = len(automaton["events"]["observable"])

    msg = menu_msg + str(num_obs - 1) + menu_msg_2
    display_menu(msg)

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
