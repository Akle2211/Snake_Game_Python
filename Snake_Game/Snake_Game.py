# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
# 28 april 2018

###IMPORTS###
from graphics import *
import time
from random import randint


###FUNCTIONS###

# return where to add a pixel
def amt_to_add(direction, x_or_y):
    if direction == 1 and x_or_y == 'x' or direction == 2 and x_or_y == 'y':
        return 1    # right or down
    elif direction == 3 and x_or_y == 'x' or direction == 0 and x_or_y == 'y':
        return -1   # left or up
    else:
        return 0    # no keys pressed, keep direction the same


# clears all that is in the window
# https://stackoverflow.com/questions/45517677/graphics-py-how-to-clear-the-window
def clear(win):
    for item in win.items[:]:
        item.undraw()
    # win.update()


def check_key(k, direction):
    if k == "Right":
        if direction != 3:  # check if snake isn'# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
# 28 april 2018

###IMPORTS###
from graphics import *
import time
from random import randint


###FUNCTIONS###

# return where to add a pixel
def amt_to_add(direction, x_or_y):
    if direction == 1 and x_or_y == 'x' or direction == 2 and x_or_y == 'y':
        return 1    # right or down
    elif direction == 3 and x_or_y == 'x' or direction == 0 and x_or_y == 'y':
        return -1   # left or up
    else:
        return 0    # no keys pressed, keep direction the same


# clears all that is in the window
# https://stackoverflow.com/questions/45517677/graphics-py-how-to-clear-the-window
def clear(win):
    for item in win.items[:]:
        item.undraw()
    # win.update()


def check_key(k, direction):
    if k == "Right":
        if direction != 3:  # check if snake isn't going left
            return 1
        return direction

    elif k == "Left":
        if direction != 1:  # check if snake isn't going right
            return 3
        return direction

    elif k == "Up":
        if direction != 2:  # check if snake isn't going down
            return 0
        return direction

    elif k == "Down":
        if direction != 0:  # check if snake isn't going up
            return 2
        return direction

    else:
        return direction


def rand_food_pos():
    temp = [randint(0, size_of_win-1), randint(0, size_of_win-1)]
    return temp


def drawing_pixel(to_draw, color):
    for sub_list in to_draw:
        # draw food:
        if type(sub_list) is not list:
            sub_list = to_draw
        # draw snake body:
        xcoord = sub_list[0]*step
        ycoord = sub_list[1]*step
        a = Rectangle(Point(xcoord, ycoord), Point(xcoord + step, ycoord + step))
        a.setFill(color)
        a.draw(win)



###VARIABLES###
step = 10
size_of_win = width = height = 40
win = GraphWin('SNAKE', width*step, height*step, autoflush=False)
win.setBackground('white')

food = rand_food_pos()
doexit = False  # for  exiting the game loop
direction = 0  # 0 up, 1 right, 2 down, 3 left

snakearray = [[10, 10]]  # first is the head of the snake

fps = 0.005  # decrease me to make game faster
refreshrate = 1/fps
timeOld = round(time.time() * 1000)


###RUNNING###
while doexit == False:  # This is the game loop.
    timeCurrent = round(time.time() * 1000)

    if timeCurrent-timeOld > refreshrate:  # Frames per second stuff
        timeOld = timeCurrent
        clear(win)

        c = Rectangle(Point(0, 0), Point(400, 400))
        c.setFill('white')
        c.draw(win)  # clear screen

        headnewposarray = [snakearray[0][0] +
                           amt_to_add(direction, 'x'), snakearray[0][1] + amt_to_add(direction, 'y')]

        snakearray.insert(0, headnewposarray)  # add new first element to the array
        del snakearray[len(snakearray)-1]  # delete the last element on that copied array

        drawing_pixel(snakearray, 'black')

        drawing_pixel(food, 'red')

        update()

        if snakearray[0][0] == food[0] and snakearray[0][1] == food[1]:  # check if the food has been eaten
            food = rand_food_pos()
            print("YUM")
            # add the latest element to the snake's body
            snakearray.append(snakearray[len(snakearray)-1])

        k = win.checkKey()  # register the last key that was pressed
        if k == "e":
            doexit = True  # Click e to exit!
        direction = check_key(k, direction)


win.getMouse()  # click mouse to close the game
win.close()
print("DONE")
# checkKey() returns the last key that was presssed
t going left
            return 1
        else:
            return direction
    elif k == "Left":
        if direction != 1:  # check if snake isn't going right
            return 3
        else:
            return direction
    elif k == "Up":
        if direction != 2:  # check if snake isn't going down
            return 0
        else:
            return direction
    elif k == "Down":
        if direction != 0:  # check if snake isn't going up
            return 2
        else:
            return direction
    else:
        return direction


def rand_food_pos():
    temp = [randint(0, size_of_win-1), randint(0, size_of_win-1)]
    return temp


def drawing_pixel(to_draw, color):
    for sub_list in to_draw:
        # draw food:
        if type(sub_list) is not list:
            sub_list = to_draw
        # draw snake body:
        xcoord = sub_list[0]*step
        ycoord = sub_list[1]*step
        a = Rectangle(Point(xcoord, ycoord), Point(xcoord + step, ycoord + step))
        a.setFill(color)
        a.draw(win)



###VARIABLES###
step = 10
size_of_win = width = height = 40
win = GraphWin('SNAKE', width*step, height*step, autoflush=False)
win.setBackground('white')

food = rand_food_pos()
doexit = False  # for  exiting the game loop
direction = 0  # 0 up, 1 right, 2 down, 3 left

snakearray = [[10, 10]]  # first is the head of the snake

fps = 0.005  # decrease me to make game faster
refreshrate = 1/fps
timeOld = round(time.time() * 1000)


###RUNNING###
while doexit == False:  # This is the game loop.
    timeCurrent = round(time.time() * 1000)

    if timeCurrent-timeOld > refreshrate:  # Frames per second stuff
        timeOld = timeCurrent
        clear(win)

        c = Rectangle(Point(0, 0), Point(400, 400))
        c.setFill('white')
        c.draw(win)  # clear screen

        headnewposarray = [snakearray[0][0] +
                           amt_to_add(direction, 'x'), snakearray[0][1] + amt_to_add(direction, 'y')]

        snakearray.insert(0, headnewposarray)  # add new first element to the array
        del snakearray[len(snakearray)-1]  # delete the last element on that copied array

        drawing_pixel(snakearray, 'black')

        drawing_pixel(food, 'red')
        # b = Rectangle(Point(food[0]*step, food[1]*step),
        #               Point(food[0]*step+step, food[1]*step+step))
        # b.setFill('red')
        # b.draw(win)  # draw food

        update()

        if snakearray[0][0] == food[0] and snakearray[0][1] == food[1]:  # check if the food has been eaten
            food = rand_food_pos()
            print("YUM")
            # add the latest element to the snake's body
            snakearray.append(snakearray[len(snakearray)-1])

        k = win.checkKey()  # register the last key that was pressed
        if k == "e":
            doexit = True  # Click e to exit!
        direction = check_key(k, direction)


win.getMouse()  # click mouse to close the game
win.close()
print("DONE")
# checkKey() returns the last key that was presssed
