from time import sleep


sleep_time = 0.05


def show_error(message):
    sleep(sleep_time)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sleep(sleep_time)
    print(message)
    sleep(sleep_time)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sleep(sleep_time)


def show_notification(message):
    sleep(sleep_time)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sleep(sleep_time)
    print(message)
    sleep(sleep_time)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sleep(sleep_time)