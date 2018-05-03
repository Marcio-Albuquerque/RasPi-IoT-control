#!/usr/bin/env python
#-*- coding: utf-8 -*-

# ********************************************   
# *    Program for controlling an air pump   * 
# *       Ant. Marcio A. A. 2018             *  
# *     o.marcio.albu@gmail.com              *  
# ********************************************     

####
# Main Control Structure
####

#*#*#*#*#
# * TODO
# V 0.1
# * Implement on / off motor DC with object-oriented python (Check);
# * Implement button push On/ Off (Check);
# * Implement LCD (Check);
# * Implement simple graphical interface (Check).
#*#*#*#*#

from motor import Motor
from lcd import LCD
import RPi.GPIO as GPIO
import time

import logging
from threading import Thread
import time
close = False

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buttonPIN = 11

GPIO.setup(buttonPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

objMotor = Motor(False) #Default startup - Off
objLCD = LCD()

class Hardware(Thread):
    def run(self):
        objLCD.setMessagem(">     Hello    <", 1)
        while True: #Loop programe
            if close == True:
                    break
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
        
        

class ControMotorApp(object):
    
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("graphic.glade")
        self.window = builder.get_object("id_windows")
        self.about = builder.get_object("id_about_programe")
        self.label = builder.get_object("id_label_status")
        self.window.show()
        builder.connect_signals({"gtk_main_quit": Gtk.main_quit,
                                "on_id_Tog_Button_clicked": self.start_stop,
                                "on_about_activate": self.about_window,
                                })
        #threading.Thread(target=loop).start()

    def start_stop(self, button):
        if button.get_active():
            button.set_label("Desligar")
            self.label.set_text("Motor: Ligado") 
            print("On")

            objLCD.setMessagem("Motor: Online", 2)
            objMotor.setStateMotor(True)
            objMotor.setActionMotor()
            
            
        else:
            button.set_label("Ligar")
            self.label.set_text("Motor: Desligado") 
            print("Off") 

            objLCD.setMessagem("Motor: Offline", 2)
            objMotor.setStateMotor(False)
            objMotor.setActionMotor() 


    def about_window(self, widget):
        """Função para exibir a Janela Sobre do programa"""
        print("aqui")
        self.about.run()
        self.about.hide()


if __name__ == "__main__":
    
    logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",format="%(asctime)-15s %(levelname)-8s %(message)s")
    logging.info("Execução do programa")
    
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, GdkPixbuf, GObject, GLib, Gio
        
    try:
        objcThread = Hardware()
        objcThread.start()
       
        GObject.threads_init()
        app = ControMotorApp()
        Gtk.main()
        close = True
        GPIO.cleanup()
        LCD().setFinish()
                        
        #threading.Thread(target=loop).stop()        
    except KeyboardInterrupt:
        pass 

    