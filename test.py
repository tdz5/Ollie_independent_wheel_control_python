import pygame
from pygame.locals import *
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()
try:
    pygame.joystick.Joystick(0).init
except:
    print("no joystick")
joystick = pygame.joystick.Joystick(0)
axco = joystick.get_numaxes()
print(axco)
done = False
while not done:
    joystick = pygame.joystick.Joystick(0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    dat = ("")
    for i in range(axco):
        val = joystick.get_axis(i)
        dat = (dat + "Axis(" + str(i) + ") = " + str(val) + "   ")
    print(dat)

