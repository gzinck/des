from time import sleep


sleep_time = 0.05


def display_menu(message):
    print("\n")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    sleep(sleep_time)
    for line in message.splitlines():
        if len(line) != 0:
            print(line)
            sleep(sleep_time)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    sleep(sleep_time)