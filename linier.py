print("Hello there")
print("General Kenobi")
import pygame
from pygame.locals import *
from sys import exit
from bluepy import btle
import struct
import Ollie_driver
ollie = Ollie_driver.Sphero()
ollie.connect()
pygame.init()
pygame.joystick.init()
brake = True # determens if 0 is brake of roll
error = 0.1 #margin for error for stick drift
r_axis = 1 #Defines what axis of the controler to lisen to
l_axis = 4 #Defalt config is for DUALSHOCK 3
clock = pygame.time.Clock()

def mode(joy, br, err):
    if(-joy > err):
        mode = 0x01
    elif(-joy < -err):
        mode = 0x02
    else:
        if br:
            mode = 0x03
        else:
            mode = 0x00
    ret = int(255 * abs(joy))
    return(mode, ret)

try:
    pygame.joystick.Joystick(0).init
except:
    print("no joystick")
    exit()


done = False
while not done:
    joystick = pygame.joystick.Joystick(0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    rjoy = joystick.get_axis(r_axis)
    ljoy = joystick.get_axis(l_axis)
    ollie.set_raw_motor_values(mode(ljoy, brake, error), mode(rjoy, brake, error))
