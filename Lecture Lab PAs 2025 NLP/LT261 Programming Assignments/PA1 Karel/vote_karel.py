from stanfordkarel import *

def main():
    # Move Up
    turn_left() 
    while facing_north() and front_is_clear() : 
        move()
        if front_is_blocked() : 
            turn_right()
        
    # diagonal \ L2R
    while front_is_clear() and right_is_clear():
        put_beeper()
        move()
        turn_right()
        move()
        turn_left()
    put_beeper()
    
    ## rotate 180 
    turn_left()
    turn_left()
    
    ## move until blocked
    while facing_west() and front_is_clear() : 
        move()
        if front_is_blocked() : 
            turn_right()
         
    ## diagonal / L2R
    while front_is_clear() and right_is_clear():
        put_beeper()
        move()
        turn_right()
        move()
        turn_left()
    put_beeper()
    
def turn_right() : 
    for i in range(3) :
        turn_left()
    

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('worlds/5x5.w')