# Race:bit - A racing game for Micro:bit 
# version 1.0 - by zelacerda

from microbit import *
import random

lines = ['00555','50055','55005','55500'] # Possible track lines (0 = track)
state = 0 # Game start

def game_start():
    global track, p, car, difficult, state
    track = '00000:00000:00000:00000:00000' # Initial track state
    display.show(['3', '2', '1'],delay=800) # Countdown
    difficult = 0 # Game speed
    car = 2 # X position of car
    p = random.randint(0,3) # Choose an initial track line
    state = 1 # Game run

def game_run():
    global track, p, car, difficult, state
    p = random.choice([i for i in [p-1,p,p+1] if i>=0 and i<4]) # Change line
    track = lines[p] + ':' + track[:-6] # Update track with a new line on top
    if button_a.is_pressed(): car = max(0, car-1) # Move left
    if button_b.is_pressed(): car = min(4, car+1) # Move right
    if track[-5:][car] != '0': # Car collided
        state = 2 # Game Over
    else: # Car on track
        display.show(Image(track))
        display.set_pixel(car,4,9)
        sleep(300-difficult)
        difficult += 1

def game_over():
    global state, difficult
    display.scroll('SCORE:%s ' % difficult, delay=80, wait=False, loop=True)
    sleep(1000)
    while not (button_a.is_pressed() or button_b.is_pressed()):
        pass # Button A or B restart the game  
    state = 0

while True:
    if   state == 0: game_start()
    elif state == 1: game_run()
    elif state == 2: game_over()
