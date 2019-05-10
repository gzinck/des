from time import sleep


def show_error(message):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sleep(0.2)
    print(message)
    sleep(0.2)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sleep(0.2)


def show_notification(message):
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(message)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    sleep(0.2)