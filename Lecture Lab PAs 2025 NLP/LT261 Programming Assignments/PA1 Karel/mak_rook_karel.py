from stanfordkarel import *

def main():
    turn = 1
    while True:
        drop_at_end = wang_beeper()
        if turn % 2 == 1:
            end = odd2even()
        else:
            end = even2odd()
        if end:
            break
        if drop_at_end and front_is_clear():
            move()
        turn += 1

def turn_right():
    for i in range(3):
        turn_left()

def if_front_is_clear_then_move(): # if front is clear , move
    if front_is_clear():
        move()
        return True
    return False

def wang_beeper():
    walkwalk = True
    
    if facing_east() or front_is_clear():
        put_beeper()
        
    while front_is_clear():
        if_front_is_clear_then_move()
        walkwalk = if_front_is_clear_then_move()
        if not walkwalk:
            return False
        put_beeper()
    return True

def odd2even():
    if front_is_blocked() and left_is_blocked():
        return True
    turn_left()
    move()
    turn_left()

def even2odd():
    if front_is_blocked() and right_is_blocked():
        return True
    turn_right()
    move()
    turn_right()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('worlds/5x5.w')