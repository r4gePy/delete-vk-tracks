from pyautogui import *
from time import sleep

coordinates_for_sortBtn = 1162, 619
sortBtn_reverse = 1105, 729

dict_coordinates = {
    1: (1140, 717),
    2: (1140, 772),
    3: (1140, 825),
    4: (1140, 882),
    5: (1140, 931),
    6: (1140, 986)
}


def sort_songs():
    moveTo(coordinates_for_sortBtn)
    click(coordinates_for_sortBtn)
    moveTo(sortBtn_reverse)
    click(sortBtn_reverse)


def delete_song():
    for x in range(6):
        moveTo(dict_coordinates.get(x+1))
        click(dict_coordinates.get(x+1))


for y in range(16):
    sort_songs()
    sleep(2)
    delete_song()
    press("f5")
    sleep(2)




