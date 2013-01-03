'''
Created on 29/12/2012

@author: Hernan
'''
import pygame


class Level5():
    button_sound=None
    wall_r = None
    wall_l = None
    wall_u = None
    floor= None
    door_l = None
    door_r = None
    door_intern= None
    
    def __init__(self):
        self.createLevel()
        
                
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1
    
    def update(self,screen):
        #screen.blit(self.door_intern.image,self.door_intern.rect)
        screen.blit(self.door_l.image,self.door_l.rect)
        screen.blit(self.door_r.image,self.door_r.rect)
        screen.blit(self.wall_l.image,self.wall_l.rect)
        screen.blit(self.wall_r.image,self.wall_r.rect)
        screen.blit(self.floor.image,self.floor.rect)
        screen.blit(self.wall_u.image,self.wall_u.rect)
        screen.blit(self.button_sound.image,self.button_sound.rect)
        
        
    def createLevel(self):
        self.wall_u = self.createSprite(0,0,"level5/pared_sup.jpg")
        self.wall_l = self.createSprite(0, self.wall_u.rect.bottom ,"level5/pared_izq.jpg") 
        self.door_l = self.createSprite(self.wall_l.rect.right, self.wall_u.rect.bottom, "level5/puerta_izq.jpg")
        #self.door_intern=self.createSprite(self.wall_l.rect.right,self.wall_u.rect.bottom,"level5/puerta_dentro.jpg")
        self.door_r = self.createSprite(self.door_l.rect.right, self.wall_u.rect.bottom, "level5/puerta_der.jpg")
        self.wall_r = self.createSprite(self.door_r.rect.right, self.wall_u.rect.bottom, "level5/pared_der.jpg")
        self.floor=self.createSprite(0,self.wall_l.rect.bottom-3,"level5/floor.jpg")
        self.button_sound=self.createSprite(10,10,"level1/sound.jpg")
    
    def checkMoveDoor(self,patron):
        solucion=["1","2","1","1","1","2"]
        print patron[0:6]
        if(patron==solucion):
            vx=-1
            vy=0
            self.door_l.rect.move_ip(vx,vy)
            self.door_r.rect.move_ip(-vx,vy)
