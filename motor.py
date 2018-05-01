#     /\\---/\\   ********************************************   
#    /^   ^  \\   *    Program for controlling an air pump   * 
#   ( O   O   )   *       Ant. Marcio A. A. 2018             *  
#    `.=o=__,'    *     o.marcio.albu@gmail.com              *  
#                 ********************************************     

####
# Code for control motor DC
####

##Libraries
import RPi.GPIO as GPIO
from time import sleep

##Configuration of GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

motorPIN = 7 #Pin out

GPIO.setup(motorPIN,GPIO.OUT) #Pin setup

class Motor():

    def __init__(self, bool):
        self.state = bool

    def getStateMotor(self):#If true On, if False Off
        return self.state

    def setStateMotor(self, bool):
        self.state = bool

    def setActionMotor(self):
        if self.state:
            print('Start')
            GPIO.output(motorPIN,GPIO.HIGH)
        else:
            GPIO.output(motorPIN,GPIO.LOW)
            print('Stop')