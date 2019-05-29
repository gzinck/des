from time import sleep


# Default speed at which lines appear in the CLI
sleep_time = 0.05


def show_error(message):
    """Displays an error message with standard formatting.

    Parameters
    ----------
    message : str
        The error message to display

    Returns
    -------
    None
    """
    sleep(sleep_time)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sleep(sleep_time)
    print(message)
    sleep(sleep_time)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sleep(sleep_time * 2)


def show_notification(message):
    """Displays a notification in the CLI to indicate some progress or event
    that has occurred. These should not include errors.

    Parameters
    ----------
    message : str
        The message to show the user

    Returns
    -------
    None
    """
    sleep(sleep_time)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sleep(sleep_time)
    print(message)
    sleep(sleep_time)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sleep(sleep_time * 2)
