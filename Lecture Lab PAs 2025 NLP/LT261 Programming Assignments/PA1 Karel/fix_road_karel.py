from stanfordkarel import *

def main():
    while True:
        if right_is_clear():
            leawkwa()
            termLoom()
        if front_is_clear():
            move()
        else:
            break

def leawkwa():
    for i in range(3):
        turn_left()

def termLoom():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_blocked():
            break
    turn_left()
    turn_left()
    while right_is_blocked():
        move()
    leawkwa()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('worlds/fix_road1.w')