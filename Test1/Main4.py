'''
Created on 28/12/2012

@author: Hernan
'''
import pygame
from Level4 import Level4



def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((860,578))
    c1 = pygame.time.Clock()
    l4 = Level4()
    hachaSeleccionada=False
    ventana_quebrada=pygame.image.load("level4/ventana_quebrada.jpg")
    patron=["0","0","0","0","0","0","0","0"]
    sound1=pygame.mixer.Sound("level1/acertijo1.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    flag=0
    i=0
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
                if(l4.control.rect.collidepoint(x,y)):
                    if(flag==0):
                        flag=1
                    else: 
                        flag=0
                        patron=["0","0","0","0","0","0","0","0"]
                        i=0
                if(l4.hacha.rect.collidepoint(x,y)):
                    if(hachaSeleccionada  and l4.hacha.rect.colliderect(l4.ventana)):
                        hachaSeleccionada=True
                        l4.ventana.image=ventana_quebrada
                    else: 
                        if(hachaSeleccionada  and not(l4.hacha.rect.colliderect(l4.ventana))):
                            hachaSeleccionada=False
                        else:
                            hachaSeleccionada=True
                
        c1.tick(60)
        if(hachaSeleccionada):
            x,y=pygame.mouse.get_pos()
            x=x-25
            y=y-25
            l4.hacha.rect.left,l4.hacha.rect.top=x,y
        
        l4.checkMoveDoor(patron)
        l4.moverPanel(flag)
        screen.fill((200,200,200))
        l4.update(screen)
        pygame.display.update()
        pygame.display.flip()
main()

