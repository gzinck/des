import global_settings
from cli.display.display_menu import display_menu
from cli.display.message import show_notification, show_error


# Message for the menu
menu_msg = '''
Choose if GraphViz Should Auto-Visualize
-------------------------------------------------------------------
If you choose "y", all automata imported and generated will
automatically be visualized and displayed. Otherwise, the user must
explicitly select the visualize option from the main menu. 
-------------------------------------------------------------------
y: automatically visualize
n: do not automatically visualize
e: exit
'''

menu_option = "graphviz_auto_vis"


def choose_auto_vis():
    """Presents a menu for the user to select if they wish to automatically
    visualize their automata upon import/creation.

    Returns
    -------
    bool
        Whether the setting was turned on, off, or neither (None)
    """
    display_menu(menu_msg)
    while True:
        inpt = input()
        # Check if the user wishes to quit
        inpt = inpt.lower()
        if inpt in ["y", "yes"]:
            global_settings.update(menu_option, True)
            show_notification("Auto-visualization turned on")
            return True
        elif inpt in ["n", "no"]:
            global_settings.update(menu_option, False)
            show_notification("Auto-visualization turned off")
            return False
        elif inpt in ["e", "exit"]:
            return None
        else:
            show_error("Command not recognized")


