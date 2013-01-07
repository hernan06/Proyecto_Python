'''
Created on 24/12/2012

@author: Keab
'''
import pygame
pygame.init()

class Level1():
    button=None
    button_sound=None
    wall_r = None
    wall_l = None
    wall_u = None
    door_l = None
    door_r = None
    door_intern=None
    fin=True
    check=False
    sound1=pygame.mixer.Sound("level1/acertijo1.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    (vx,vy)=(0,0)
    

    def __init__(self):
        self.createLevel()
        
                
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1
    
    def update(self,screen):
        screen.blit(self.wall_u.image,self.wall_u.rect)
        screen.blit(self.door_intern.image,self.door_intern.rect)
        screen.blit(self.door_l.image,self.door_l.rect)
        screen.blit(self.door_r.image,self.door_r.rect)
        screen.blit(self.wall_l.image,self.wall_l.rect)
        screen.blit(self.wall_r.image,self.wall_r.rect)
        screen.blit(self.button.image,self.button.rect)
        screen.blit(self.button_sound.image,self.button_sound.rect)

        
    def createLevel(self):
        self.wall_u = self.createSprite(0,0,"level1/pared_sup.jpg")
        self.door_intern=self.createSprite(320,self.wall_u.rect.bottom,"level1/puerta_dentro.jpg")
        self.door_l = self.createSprite(320, self.wall_u.rect.bottom, "level1/puerta_der.jpg")
        self.door_r = self.createSprite(self.door_l.rect.right, self.wall_u.rect.bottom, "level1/puerta_izq.jpg")
        self.wall_l = self.createSprite(0, self.wall_u.rect.bottom ,"level1/pared_izq.jpg")        
        self.wall_r = self.createSprite(self.door_r.rect.right, self.wall_u.rect.bottom, "level1/pared_der.jpg")
        self.button=self.createSprite(620,400,"level1/boton.jpg")
        self.button_sound=self.createSprite(30,30,"level1/sound.jpg")
        
        
    def checkMoveDoor(self,vx,vy):
        self.door_l.rect.move_ip(vx,vy)
        self.door_r.rect.move_ip(-vx,vy)
        self.check=True
        
        
    def checking(self, screen):
        c1 = pygame.time.Clock()
        while (True and self.fin):
            (x,y) = (0,0)
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    (x ,y) = pygame.mouse.get_pos()
                if(self.button.rect.collidepoint( x, y)):
                    pygame.mixer.music.play()
                    self.vx=-1
                if(self.button_sound.rect.collidepoint( x, y)):
                    self.sound1.play()
                if(self.door_intern.rect.collidepoint(x,y) and self.check):
                    self.fin=False
                
            c1.tick(60)
            self.checkMoveDoor(self.vx,self.vy)
            screen.fill((200,200,200))
            self.update(screen)
            pygame.display.update()
            