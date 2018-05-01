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
# * Implement button push On/ Off;
# * Implement LCD;
# * Implement simple graphical interface.
#*#*#*#*#

from motor import Motor

objMotor = Motor(False) #Default startup

try: #Interruption Structure
    while True:
        button = input("Start motor (Y/N) \n--> ")
        if button == "Y":
            objMotor.setStateMotor(True)
            objMotor.setActionMotor()
        else:
            objMotor.setStateMotor(False)
            objMotor.setActionMotor()
except KeyboardInterrupt: #Interruption Structure
    pass
    