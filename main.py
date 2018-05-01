#     /\\---/\\   ********************************************   
#    /^   ^  \\   *    Program for controlling an air pump   * 
#   ( O   O   )   *       Ant. Marcio A. A. 2018             *  
#    `.=o=__,'    *     o.marcio.albu@gmail.com              *  
#                 ********************************************     

####
# Main Control Structure
####

#*#*#*#*#
# * TODO
# V 0.1
# * Implement on / off motor DC with object-oriented python (Check);
# * Implement button push On/ Off (Check);
# * Implement LCD (Check);
# * Implement simple graphical interface.
#*#*#*#*#

from motor import Motor
from lcd import LCD
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buttonPIN = 11

GPIO.setup(buttonPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

objMotor = Motor(False) #Default startup - Off
objLCD = LCD()
try: #Interruption Structure
    objLCD.setMessagem(">     Hello    <", 1)
    while True: #Loop programe
        
        input_state = GPIO.input(buttonPIN)
        
        if input_state == False:
            print('Button Pressed')
            if objMotor.getStateMotor():           
                
                objLCD.setMessagem("Motor: Offline", 2)
                objMotor.setStateMotor(False)
                objMotor.setActionMotor()
                
            else:
                
                objLCD.setMessagem("Motor: Online", 2)
                objMotor.setStateMotor(True)
                objMotor.setActionMotor()
                
        time.sleep(0.2)

except KeyboardInterrupt: #Interruption Structure
    GPIO.cleanup()
    LCD().setFinish()
    pass 
    