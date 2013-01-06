'''
Created on 03/01/2013

@author: Hernan
'''
import pygame
from Level8 import Level8



def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((860,578))
    c1 = pygame.time.Clock()
    l8 = Level8()
    sound1=pygame.mixer.Sound("level5/acertijo5.wav")
    door_izq=pygame.mixer.Sound("level5/door_izq.wav")
    door_der=pygame.mixer.Sound("level5/door_der.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    lampara1select=False
    lampara2select=False
    lampara3select=False
    lampara4select=False
    
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if(l8.lampara1.rect.collidepoint(x,y)):
                    if(lampara1select):
                        lampara1select=False
                    else:
                        lampara1select=True
                if(l8.lampara2.rect.collidepoint(x,y)):
                    if(lampara2select):
                        lampara2select=False
                    else:
                        lampara2select=True
                if(l8.lampara3.rect.collidepoint(x,y)):
                    if(lampara3select):
                        lampara3select=False
                    else:
                        lampara3select=True
                if(l8.lampara4.rect.collidepoint(x,y)):
                    if(lampara4select):
                        lampara4select=False
                    else:
                        lampara4select=True
        c1.tick(60)
        x,y=pygame.mouse.get_pos()
        y=y+30
        if(lampara1select and l8.lampara1.rect.top<0):
            l8.lampara1.rect.bottom=y
            print y
        if(l8.lampara1.rect.top>=0):
            l8.lampara1.rect.top=-2
        if(lampara2select and l8.lampara2.rect.top<0):
            l8.lampara2.rect.bottom=y
            print y
        if(l8.lampara2.rect.top>=0):
            l8.lampara2.rect.top=-2
        if(lampara3select and l8.lampara3.rect.top<0):
            l8.lampara3.rect.bottom=y
            print y
        if(l8.lampara3.rect.top>=0):
            l8.lampara3.rect.top=-2
        if(lampara4select and l8.lampara4.rect.top<0):
            l8.lampara4.rect.bottom=y
            print y
        if(l8.lampara4.rect.top>=0):
            l8.lampara4.rect.top=-2
        solucion=l8.checkLamparas(l8.lampara1.rect.bottom,l8.lampara2.rect.bottom,l8.lampara3.rect.bottom,l8.lampara4.rect.bottom)
        l8.checkMoveDoor(solucion)
        screen.fill((200,200,200))
        l8.update(screen)
        pygame.display.update()
        pygame.display.flip()
main()

