'''
Created on 24/12/2012

@author: Keab
'''
import pygame

class Level1():
    roof = None
    button=None
    button_sound=None
    wall_r = None
    wall_l = None
    wall_u = None
    door_l = None
    door_r = None
    door_intern=None
    

    def __init__(self, screen):
        self.createLevel()
        
                
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1
    
    def update(self,screen):
        screen.blit(self.roof.image, self.roof.rect)
        screen.blit(self.wall_u.image,self.wall_u.rect)
        screen.blit(self.door_intern.image,self.door_intern.rect)
        screen.blit(self.door_l.image,self.door_l.rect)
        screen.blit(self.door_r.image,self.door_r.rect)
        screen.blit(self.wall_l.image,self.wall_l.rect)
        screen.blit(self.wall_r.image,self.wall_r.rect)
        screen.blit(self.button.image,self.button.rect)
        screen.blit(self.button_sound.image,self.button_sound.rect)

        
    def createLevel(self):
        self.roof = self.createSprite(0, 0, "level1/techo.jpg")
        self.wall_u = self.createSprite(0, self.roof.rect.bottom, "level1/pared_sup.jpg")
        self.door_intern=self.createSprite(155,self.wall_u.rect.bottom,"level1/puerta_dentro.jpg")
        self.door_l = self.createSprite(155, self.wall_u.rect.bottom, "level1/puerta_izq.jpg")
        self.door_r = self.createSprite(self.door_l.rect.right, self.wall_u.rect.bottom, "level1/puerta_der.jpg")
        self.wall_l = self.createSprite(0, self.wall_u.rect.bottom ,"level1/pared_izq.jpg")        
        self.wall_r = self.createSprite(self.door_r.rect.right, self.wall_u.rect.bottom, "level1/pared_der.jpg")
        self.button=self.createSprite(400,350,"level1/boton.jpg")
        self.button_sound=self.createSprite(0, self.roof.rect.bottom,"level1/sound.jpg")
        
        
    def checkMoveDoor(self,vx,vy):
        self.door_l.rect.move_ip(vx,vy)
        self.door_r.rect.move_ip(-vx,vy)

            