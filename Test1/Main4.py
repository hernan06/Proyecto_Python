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
    vx,vy=0,0
    sound1=pygame.mixer.Sound("level1/acertijo1.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if(x>=0):
                    pygame.mixer.music.play()
                    vx=-1
                    
        
        c1.tick(60)
        l4.checkMoveDoor(vx,vy)
        screen.fill((200,200,200))
        l4.update(screen)
        pygame.display.update()
        pygame.display.flip()
main()