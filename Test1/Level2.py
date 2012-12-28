'''
Created on 26/12/2012

@author: Hernan
'''
import pygame

class Level2():
    button_sound=None
    wall_r1 = None
    wall_l1 = None
    wall_r2 = None
    wall_l2 = None
    wall_u = None
    floor = None
    door_l = None
    door_r = None
    door_intern=None
    ball1= None
    ball2= None
    

    def __init__(self, screen):
        self.createLevel()
        
                
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1
    
    def update(self,screen):
        screen.blit(self.wall_u.image,self.wall_u.rect)
        screen.blit(self.door_l.image,self.door_l.rect)
        screen.blit(self.door_r.image,self.door_r.rect)
        screen.blit(self.wall_l1.image,self.wall_l1.rect)
        screen.blit(self.wall_l2.image,self.wall_l2.rect)
        screen.blit(self.wall_r1.image,self.wall_r1.rect)
        screen.blit(self.wall_r2.image,self.wall_r2.rect)
        screen.blit(self.floor.image,self.floor.rect)
        screen.blit(self.ball1.image,self.ball1.rect)
        screen.blit(self.ball2.image,self.ball2.rect)
        screen.blit(self.button_sound.image,self.button_sound.rect)

        
    def createLevel(self):
        self.wall_u = self.createSprite(0,0,"level2/pared_sup.jpg")
        self.door_l = self.createSprite(229, self.wall_u.rect.bottom, "level2/puerta_izq.jpg")
        self.door_r = self.createSprite(self.door_l.rect.right, self.wall_u.rect.bottom, "level2/puerta_der.jpg")
        self.wall_l1 = self.createSprite(0, self.wall_u.rect.bottom ,"level2/pared_izq1.jpg")    
        self.wall_l2 = self.createSprite(141, self.wall_u.rect.bottom ,"level2/pared_izq2.jpg")     
        self.wall_r1 = self.createSprite(self.door_r.rect.right-2, self.wall_u.rect.bottom, "level2/pared_der1.jpg")
        self.wall_r2 = self.createSprite(self.door_r.rect.right+147, self.wall_u.rect.bottom, "level2/pared_der2.jpg")
        self.floor=self.createSprite(0,self.wall_l1.rect.bottom,"level2/piso.jpg")
        self.button_sound=self.createSprite(10,10,"level1/sound.jpg")
        self.ball1=self.createSprite(self.wall_l1.rect.right,self.floor.rect.top-42,"level2/esfera.jpg")
        self.ball2=self.createSprite(self.wall_r1.rect.right,self.wall_u.rect.bottom+2,"level2/esfera.jpg")
        
        
    def checkMoveDoor(self,altura1,altura2):
        if(altura1>=180 and altura1<=224 and altura2>=375 and altura2<=424):
            print "siiii"
            vx=-1
            vy=0
            self.door_l.rect.move_ip(vx,vy)
            self.door_r.rect.move_ip(-vx,vy)