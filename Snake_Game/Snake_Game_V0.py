from graphics import *
import time
from random import randint
win = GraphWin('SNAKE', 400, 400)
win.setBackground('white')

doexit = False  # for  exiting the game loop
direction = 0  # 0 up, 1 right, 2 down, 3 left

snakearray = [[10, 10]]  # first is the head of the snake
snakearrayold = snakearray  # all elements from new will be coppied to old with exception of last element in new

food = randint(0, 9)


fps = 0.005  # increase me to make game faster
refreshrate = 1/fps
timeOld = int(round(time.time() * 1000))


def amounttoaddx(direction):  # FUNCTIONS that take in direction and return how much to change the up/down/left/right by
    if direction == 1:
        return 1
    elif direction == 3:
        return -1
    else:
        return 0


def amounttoaddy(direction):
    if direction == 0:
        return 1
    elif direction == 2:
        return -1
    else:
        return 0


while doexit == False:  # This is the game loop.
    timeCurrent = int(round(time.time() * 1000))
    if timeCurrent-timeOld > refreshrate:  # Frames per second stuff
        timeOld = timeCurrent
        c = Rectangle(Point(0, 0), Point(400, 400))
        c.setFill('white')
        c.draw(win)  # clear screen

        # move the snake's body and update the arrays
        snakearray = snakearrayold  # copy the array
        # create array for head that can be inserted
        headnewposarray = [snakearray[0][0] +
                           amounttoaddx(direction), snakearray[0][1] + amounttoaddy(direction)]
        snakearray.insert(0, headnewposarray)  # add new first element to the array
        del snakearray[len(snakearray)-1]  # delete the last element on that copied array
        snakearrayold = snakearray  # replace the old snake array with the now updated one
        for i in range(len(snakearray)):  # draw the snake
            xcoord = snakearray[i][0]*10
            ycoord = snakearray[i][1]*10
            xcoord1 = snakearray[i][0]*10 + 10
            ycoord1 = snakearray[i][1]*10 + 10
            a = Rectangle(Point(xcoord, ycoord), Point(xcoord1, ycoord1))
            a.setFill('black')
            a.draw(win)
        b = Rectangle(Point(food*10, food*10), Point(food*10+10, food*10+10))
        b.setFill('red')
        b.draw(win)  # draw food

        if snakearray[0][0] == food and snakearray[0][1] == food:  # check if the food has been eaten
            food = randint(0, 9)
            print("YUM")
            # add the latest element to the snake's body
            snakearray.append(snakearray[len(snakearray)-1])
        k = win.checkKey()  # register the last key that was pressed
        if k == "e":
            doexit = True  # Click e to exit!
        if k == "Right":
            if direction != 3:  # check if snake isn't going left
                direction = 1
        if k == "Left":
            if direction != 1:  # check if snake isn't going right
                direction = 3
        if k == "Up":
            if direction != 0:  # check if snake isn't going down
                direction = 2
        if k == "Down":
            if direction != 2:  # check if snake isn't going up
                direction = 0

win.getMouse()  # click mouse to close the game
win.close()
print("DONE")
# checkKey() returns the last key that was presssed
