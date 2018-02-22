#!/usr/bin/python

import PiMotor
import time

#Name of Individual MOTORS 
m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

#To Drive Motors
motorFront = PiMotor.LinkedMotors(m1,m2)

motorBack = PiMotor.LinkedMotors(m3,m4)

#Names for Individual Arrows
ab = PiMotor.Arrow(1) # South
al = PiMotor.Arrow(2) # Left
af = PiMotor.Arrow(3) # North
ar = PiMotor.Arrow(4) # South

##This segment drives the motors in the direction listed below:
## forward in percentage(0-100)

try:
    while True:
#-----------To Drive the Motors Forward------------# 
        print(" Robot Moving Forward ")
        af.on()
        motorFront.forward(100)
		motorBack.reverse (100)
        time.sleep(5)
#--------------------------------------------------#
except KeyboardInterrupt:
    GPIO.cleanup()



