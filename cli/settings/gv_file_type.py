import global_settings
from cli.display.display_menu import display_menu
from cli.display.message import show_notification, show_error


# Message for the menu
menu_msg = '''
Choose GraphViz File Output Type
-------------------------------------------------------------------
Type the index of the option you want to choose and press enter.
-------------------------------------------------------------------
'''
menu_msg_2 = 'e: exit'
file_types = ["pdf", "svg", "jpeg", "png"]
menu_option = "graphviz_file_type"


def get_file_type_options():
    """Turns all file type options into a string for displaying to the user.

    Returns
    -------
    str
        String representation of all file types that can be output
    """
    curr_type = global_settings.settings[menu_option]
    msg = ""
    for i in range(len(file_types)):
        if curr_type == file_types[i]:
            msg += str(i) + " " + file_types[i] + " SELECTED\n"
        else:
            msg += str(i) + " " + file_types[i] + "\n"
    return msg


def choose_gv_file_type():
    """Presents a menu for the user to select their desired graphviz file output
    type (pdf, png, jpeg...)

    Returns
    -------
    int
        The selected index, or None if quit
    """
    display_menu(menu_msg + get_file_type_options() + menu_msg_2)
    while True:
        inpt = input()
        try:
            # If we get a good number, select it!
            if int(inpt) in range(len(file_types)):
                selected = file_types[int(inpt)]
                show_notification("Selected:\n" + selected)
                global_settings.update(menu_option, selected)
                return int(inpt)
            else:
                show_error("Not a valid observer index")
        except ValueError:
            # Check if the user wishes to quit
            inpt = inpt.lower()
            if inpt in ["e", "exit"]:
                return None
            else:
                show_error("Command not recognized")

