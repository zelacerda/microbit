from microbit import *

gesture = ''

while True:
    current = accelerometer.current_gesture()
    if gesture != current:
        gesture = current
        uart.write(str(gesture)+'\n')
