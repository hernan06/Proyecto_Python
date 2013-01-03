'''
Created on 02/01/2013

@author: Hernan
'''
import pygame
from Level7 import Level7



def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((860,578))
    c1 = pygame.time.Clock()
    l7 = Level7()
    patron=["0","0","0","0","0","0","0","0"]
    flag=0
    sound1=pygame.mixer.Sound("level5/acertijo5.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    raton_seleccionado=False
    x,y=0,0
    dish1=False
    dish2=False
    dish3=False
    i=0
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()
            if events.type == pygame.KEYDOWN:
                if(flag==1 and events.key == pygame.K_1):
                    patron.pop(i)
                    patron.insert(i,"1")
                    if(i<4):
                        i=i+1
                if(flag==1 and events.key == pygame.K_2):
                    patron.pop(i)
                    patron.insert(i,"2")
                    if(i<4):
                        i=i+1
                if(flag==1 and events.key == pygame.K_3):
                    patron.pop(i)
                    patron.insert(i,"3")
                    if(i<4):
                        i=i+1
                if(flag==1 and events.key == pygame.K_4):
                    patron.pop(i)
                    patron.insert(i,"4")
                    if(i<4):
                        i=i+1
                if(flag==1 and events.key == pygame.K_5):
                    patron.pop(i)
                    patron.insert(i,"5")
                    if(i<4):
                        i=i+1
                if(flag==1 and events.key == pygame.K_6):
                    patron.pop(i)
                    patron.insert(i,"6")
                    if(i<4):
                        i=i+1
                if(flag==1 and events.key == pygame.K_7):
                    patron.pop(i)
                    patron.insert(i,"7")
                    if(i<4):
                        i=i+1
                if(flag==1 and events.key == pygame.K_8):
                    patron.pop(i)
                    patron.insert(i,"8")
                    if(i<4):
                        i=i+1
                if(flag==1 and events.key == pygame.K_9):
                    patron.pop(i)
                    patron.insert(i,"9") 
                    if(i<4):
                        i=i+1   
            if events.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if(l7.control.rect.collidepoint(x,y)):
                    if(flag==0):
                        flag=1
                    else: 
                        flag=0
                        patron=["0","0","0","0","0","0","0","0"]
                        i=0  
                if(l7.raton.rect.collidepoint(x,y)):
                    if(not(raton_seleccionado)):
                        raton_seleccionado=True
                    else:
                        if(l7.plato1.rect.collidepoint(x,y) and not(dish1)):
                            dish1=True
                            l7.snake.rect.left=l7.snake.rect.left-200
                            
                        if(l7.plato2.rect.collidepoint(x,y) and not(dish2)):
                            dish2=True
                            l7.snake.rect.left=l7.snake.rect.left-200
                            
                        if(l7.plato3.rect.collidepoint(x,y) and not(dish3)):
                            dish3=True
                            l7.snake.rect.left=l7.snake.rect.left-200
                        l7.raton.rect.left,l7.raton.rect.top=-68,l7.floor.rect.top
                        raton_seleccionado=False
        
        if(raton_seleccionado):
            x,y=pygame.mouse.get_pos()
            x=x-25
            y=y-25
            l7.raton.rect.left,l7.raton.rect.top=x,y
        c1.tick(60)
        l7.checkMoveDoor(patron)
        l7.moverRaton()
        l7.moverPanel(flag)
        screen.fill((200,200,200))
        l7.update(screen)
        pygame.display.update()
        pygame.display.flip()
main()



