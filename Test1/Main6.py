'''
Created on 31/12/2012

@author: Hernan
'''
import pygame
from Level6 import Level6



def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((860,578))
    c1 = pygame.time.Clock()
    l6 = Level6()
    patron=["0","0","0","0","0","0","0","0"]
    sound1=pygame.mixer.Sound("level1/acertijo1.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    i=0
    flag=0
    cono1_seleccionado=False
    cono2_seleccionado=False
    toma_seleccionado=False
    muro1_seleccionado=False
    muro2_seleccionado=False
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()
            if events.type == pygame.KEYDOWN:
                if(flag==1 and events.key == pygame.K_1):
                    patron.pop(i)
                    patron.insert(i,"1")
                    if(i<7):
                        i=i+1
                if(flag==1 and events.key == pygame.K_2):
                    patron.pop(i)
                    patron.insert(i,"2")
                    if(i<7):
                        i=i+1
                if(flag==1 and events.key == pygame.K_3):
                    patron.pop(i)
                    patron.insert(i,"3")
                    if(i<7):
                        i=i+1
                if(flag==1 and events.key == pygame.K_4):
                    patron.pop(i)
                    patron.insert(i,"4")
                    if(i<7):
                        i=i+1
                if(flag==1 and events.key == pygame.K_5):
                    patron.pop(i)
                    patron.insert(i,"5")
                    if(i<7):
                        i=i+1
                if(flag==1 and events.key == pygame.K_6):
                    patron.pop(i)
                    patron.insert(i,"6")
                    if(i<7):
                        i=i+1
                if(flag==1 and events.key == pygame.K_7):
                    patron.pop(i)
                    patron.insert(i,"7")
                    if(i<7):
                        i=i+1
                if(flag==1 and events.key == pygame.K_8):
                    patron.pop(i)
                    patron.insert(i,"8")
                    if(i<7):
                        i=i+1
                if(flag==1 and events.key == pygame.K_9):
                    patron.pop(i)
                    patron.insert(i,"9") 
                    if(i<7):
                        i=i+1   
            if events.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if(l6.control.rect.collidepoint(x,y)):
                    if(flag==0):
                        flag=1
                    else: 
                        flag=0
                        patron=["0","0","0","0","0","0","0","0"]
                        i=0
                if(l6.cono1.rect.collidepoint(x,y)):
                    if(not(cono1_seleccionado)):
                        cono1_seleccionado=True
                    else:
                        cono1_seleccionado=False
                if(l6.cono2.rect.collidepoint(x,y)):
                    if(not(cono2_seleccionado)):
                        cono2_seleccionado=True
                    else:
                        cono2_seleccionado=False
                if(l6.muro1.rect.collidepoint(x,y)):
                    if(not(muro1_seleccionado)):
                        muro1_seleccionado=True
                    else:
                        muro1_seleccionado=False
                if(l6.muro2.rect.collidepoint(x,y)):
                    if(not(muro2_seleccionado)):
                        muro2_seleccionado=True
                    else:
                        muro2_seleccionado=False
                if(l6.toma.rect.collidepoint(x,y)):
                    if(not(toma_seleccionado)):
                        toma_seleccionado=True
                    else:
                        toma_seleccionado=False
                    
        
        c1.tick(60)
        if(cono1_seleccionado):
            x,y=pygame.mouse.get_pos()
            x=x-25
            y=y-25
            l6.cono1.rect.left,l6.cono1.rect.top=x,y
        if(cono2_seleccionado):
            x,y=pygame.mouse.get_pos()
            x=x-25
            y=y-25
            l6.cono2.rect.left,l6.cono2.rect.top=x,y
        if(muro1_seleccionado):
            x,y=pygame.mouse.get_pos()
            x=x-25
            y=y-25
            l6.muro1.rect.left,l6.muro1.rect.top=x,y
        if(muro2_seleccionado):
            x,y=pygame.mouse.get_pos()
            x=x-25
            y=y-25
            l6.muro2.rect.left,l6.muro2.rect.top=x,y
        if(toma_seleccionado):
            x,y=pygame.mouse.get_pos()
            x=x-25
            y=y-25
            l6.toma.rect.left,l6.toma.rect.top=x,y
        l6.checkMoveDoor(patron)
        l6.moverPanel(flag)
        screen.fill((200,200,200))
        l6.update(screen)
        pygame.display.update()
        pygame.display.flip()
main()



