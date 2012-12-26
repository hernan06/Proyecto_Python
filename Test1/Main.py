'''
Created on 24/12/2012

@author: Keab
'''
import pygame
from Level1 import Level1



def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((500,500))
    c1 = pygame.time.Clock()
    l1 = Level1(screen)
    (x,y) = (0,0)
    vx,vy=0,0
    sound1=pygame.mixer.Sound("level1/acertijo1.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if(l1.button.rect.collidepoint(x,y)):
                    pygame.mixer.music.play()
                    vx=-1
                if(l1.button_sound.rect.collidepoint(x,y)):
                    sound1.play()
                    
        
        c1.tick(60)
        l1.checkMoveDoor(vx,vy) 
        screen.fill((200,200,200))
        l1.update(screen)
        pygame.display.update()
    
main()



