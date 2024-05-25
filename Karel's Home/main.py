from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    # add your code here
    for i in range(2):
        move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_right()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    for i in range(2):
        move()
    for i in range(2):
        turn_left()
def turn_right():
    for i in range(3):
        turn_left()
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()