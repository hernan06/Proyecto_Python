'''
Created on 27/12/2012

@author: Hernan
'''
import pygame
from Level2 import Level2

def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((860,578))
    c1 = pygame.time.Clock()
    l2 = Level2(screen)
    (x,y) = (0,0)
    vx,vy=0,0
    ball1_selected=False
    ball2_selected=False
    sound1=pygame.mixer.Sound("level1/acertijo1.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if(l2.ball1.rect.collidepoint(x,y) and not(ball2_selected)):
                    if(ball1_selected):
                        ball1_selected=False
                    else:
                        ball1_selected=True
                if(l2.ball2.rect.collidepoint(x,y) and not(ball1_selected)):
                    if(ball2_selected):
                        ball2_selected=False
                    else:
                        ball2_selected=True
                    
        c1.tick(60)
        oldy=l2.ball1.rect.top
        oldy2=l2.ball2.rect.top
        if(ball1_selected):
            x,y=pygame.mouse.get_pos()
            l2.ball1.rect.top=y
            print l2.ball1.rect.top
            if(l2.ball1.rect.colliderect(l2.wall_u.rect) or l2.ball1.rect.colliderect(l2.floor.rect)):
                l2.ball1.rect.top=oldy
        if(ball2_selected):
            x,y=pygame.mouse.get_pos()
            l2.ball2.rect.top=y
            print l2.ball2.rect.top
            if(l2.ball2.rect.colliderect(l2.wall_u.rect) or l2.ball2.rect.colliderect(l2.floor.rect)):
                l2.ball2.rect.top=oldy2
            
        l2.checkMoveDoor(l2.ball1.rect.top,l2.ball2.rect.top)
        screen.fill((255,255,255))
        l2.update(screen)
        pygame.display.update()
        pygame.display.flip()
main()



