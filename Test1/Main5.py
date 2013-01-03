'''
Created on 29/12/2012

@author: Hernan
'''
import pygame
from Level5 import Level5



def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((860,578))
    c1 = pygame.time.Clock()
    l5 = Level5()
    patron=[]
    sound1=pygame.mixer.Sound("level5/acertijo5.wav")
    door_izq=pygame.mixer.Sound("level5/door_izq.wav")
    door_der=pygame.mixer.Sound("level5/door_der.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    i=0
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if(l5.door_l.rect.collidepoint(x,y)):
                    door_izq.play()
                    patron.append("1")
                    if(i<6):
                        i=i+1
                    else: 
                        i=0
                        patron=[]
                        patron.append("1")
                if(l5.door_r.rect.collidepoint(x,y)):
                    door_der.play()
                    patron.append("2")
                    if(i<6):
                        i=i+1
                    else: 
                        i=0
                        patron=[]
                        patron.append("2")
                if(l5.button_sound.rect.collidepoint(x,y)):
                    sound1.play()
                    
        
        c1.tick(60)
        l5.checkMoveDoor(patron)
        screen.fill((200,200,200))
        l5.update(screen)
        pygame.display.update()
        pygame.display.flip()
main()



