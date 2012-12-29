'''
Created on 27/12/2012

@author: Hernan
'''
import pygame
from Level3 import Level3



def main():
    
    pygame.init()
    
    blanco=pygame.image.load("level3/circulo_blanco.png")
    rojo=pygame.image.load("level3/circulo_rojo.png")
    patron=["0","0","0","0","0","0","0","0"]
    patron2=["0","0","0","0","0","0","0","0"]
    screen = pygame.display.set_mode((860,578))
    c1 = pygame.time.Clock()
    l3 = Level3()
    (x,y) = (0,0)
    sound1=pygame.mixer.Sound("level1/acertijo1.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                for circle in l3.List1:
                    if(circle.rect.collidepoint(x,y)):
                        i=l3.List1.index(circle)
                        print i
                        if(circle.image==blanco):
                            circle.image=rojo
                            patron.pop(i)
                            patron.insert(i,"1")
                            print patron[0:8]
                        else: 
                            circle.image=blanco
                            patron.pop(i)
                            patron.insert(i,"0")
                            print patron[0:8]
                            
                for circle2 in l3.List2:
                    if(circle2.rect.collidepoint(x,y)):
                        i=l3.List2.index(circle2)
                        if(circle2.image==blanco):
                            circle2.image=rojo
                            patron2.pop(i)
                            patron2.insert(i,"1")
                        else: 
                            circle2.image=blanco
                            patron2.pop(i)
                            patron2.insert(i,"0")
                    
                    
        
        c1.tick(60)
        l3.checkMoveDoor(patron,patron2)
        screen.fill((200,200,200))
        l3.update(screen)
        pygame.display.update()
        pygame.display.flip()
        
main()