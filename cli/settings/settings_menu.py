from cli.display.display_menu import display_menu
from cli.display.message import show_error
from cli.settings.gv_file_type import choose_gv_file_type
from cli.settings.gv_auto_vis import choose_auto_vis


# The message describing what the menu is for
menu_msg = '''
Settings Menu
-------------------------------------------------------------------
Type one of the below commands to change default settings
-------------------------------------------------------------------
f: change the default file output type for GraphViz visualization
   of automata
a: enable/disable auto-visualization of automata on import and
   generation
'''


def settings_menu():
    """Opens a menu with options for different settings which can be edited. It
    changes the default for all future sessions as well.

    Returns
    -------
    None
    """
    display_menu(menu_msg)

    inpt = input().lower()

    # Choose which operation to perform
    if inpt in ["f", "file"]:
        choose_gv_file_type()
    elif inpt in ["a"]:
        choose_auto_vis()
    elif inpt in ["e", "exit"]:
        pass
    else:
        show_error("Command not recognized")