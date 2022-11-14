import msvcrt
import os
import random

my_position = [1, 1]
tail_lenght = 0
tail = []
POS_X = 0
POS_Y = 1

my_position[POS_X]
my_position[POS_Y]

map_objects = []

score = 0
new_score = None


NUMBER_OBJECTS = 10



MAP_WIDTH = 20
MAP_HEIGHT = 10

#Main loop
while True:
    # Generator of random objects
    while len(map_objects) < NUMBER_OBJECTS:
        object_position_x = random.randint(0, MAP_WIDTH - 1)
        object_position_y = random.randint(0, MAP_HEIGHT - 1)
        random_object = [object_position_x, object_position_y]
        if random_object not in map_objects \
                and random_object != my_position \
                and random_object:
            map_objects.append(random_object)

    print("+" + "-" * (MAP_WIDTH) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1
                    score += 50

            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * (MAP_WIDTH) + "+")

    if my_position in tail:
        print("GAME OVER")
        print("SCORE: {}".format(score))
        exit()

#Controles
    direction = msvcrt.getwch()
    new_position = None

    if direction == "w" or direction == "W":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s" or direction == "S":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a" or direction == "A":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d" or direction == "D":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q" or direction == "Q":
        break

    else:
        pass

    if new_position:
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position = new_position

    os.system("cls")
