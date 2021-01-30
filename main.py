import pyautogui as gui
import time


main_list = []

# Read in complete works of william shakespeare
with open('/Users/attis/Desktop/shakespeare.txt', 'r') as file:
    list_iteration = [line.rstrip() for line in file]
    for line in list_iteration:
        line = line.strip("\\")
        main_list.append(line)


def auto_texter(list_item):
    gui.write(list_item)
    gui.press("enter")


# Calls the function every 3 seconds until program break
while True:
    for line in main_list:
        time.sleep(3)
        auto_texter(line)