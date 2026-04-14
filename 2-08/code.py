"""
Created by Elliott Roach
Created on Mar 2026
This is a sonar distance sensors and moves a servo if under 50 cm.
"""

import board
import digitalio
import time
import pwmio
from adafruit_motor import servo
import analogio

# setup
data_wire = pwmio.PWMOut(board.GP11, duty_cycle= 2 ** 15, frequency= 50)
my_servo = servo.Servo(data_wire)
my_servo.angle = 0
servo_angle = 0
ratio = 65535 / 180
potentiometer = analogio.AnalogIn(board.GP26_A0)


# infinte loop
while True:
    try:
            servo_angle = potentiometer / ratio
            my_servo.angle = servo_angle
    except RuntimeError:
        print("Error")
    time.sleep(0.1)
