from time import sleep


# The default speed for each line appearing on the command line
sleep_time = 0.025


def display_menu(message):
    """Displays a menu with a given message. Each menu has a standard speed at
    which it appears and a standard formatting, hence this helper method.

    Parameters
    ----------
    message : str
        The message to be delivered in the menu

    Returns
    -------
    None
    """
    print("\n")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    sleep(sleep_time)
    for line in message.splitlines():
        if len(line) != 0:
            print(line)
            sleep(sleep_time)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    sleep(sleep_time * 2)