'''
Created on 27/12/2012

@author: Hernan
'''
import pygame
from compiler.ast import List


class Level3():
    button_sound=None
    wall_r = None
    wall_l = None
    wall_u = None
    floor= None
    door_l = None
    door_r = None
    door_intern=None
    List1=[]
    List2=[]

    def __init__(self):
        self.createLevel()
        
                
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1
    
    def update(self,screen):
        screen.blit(self.door_intern.image,self.door_intern.rect)
        screen.blit(self.door_l.image,self.door_l.rect)
        screen.blit(self.door_r.image,self.door_r.rect)
        screen.blit(self.wall_l.image,self.wall_l.rect)
        screen.blit(self.wall_r.image,self.wall_r.rect)
        screen.blit(self.floor.image,self.floor.rect)
        screen.blit(self.wall_u.image,self.wall_u.rect)
        screen.blit(self.button_sound.image,self.button_sound.rect)
        for circle in self.List1:
            screen.blit(circle.image,circle.rect)
        for circle1 in self.List2:
            screen.blit(circle1.image,circle1.rect)
        
        
    def createLevel(self):
        self.wall_u = self.createSprite(0,0,"level3/pared_sup.jpg")
        self.wall_l = self.createSprite(0, self.wall_u.rect.bottom ,"level3/pared_izq.jpg") 
        self.door_l = self.createSprite(self.wall_l.rect.right-1, self.wall_u.rect.bottom-1, "level3/puerta_izq.png")
        self.door_intern=self.createSprite(self.wall_l.rect.right,self.wall_u.rect.bottom,"level3/puerta_dentro.jpg")
        self.door_r = self.createSprite(self.door_l.rect.right, self.wall_u.rect.bottom-1, "level3/puerta_der.png")
        self.wall_r = self.createSprite(self.door_r.rect.right-1, self.wall_u.rect.bottom, "level3/pared_der.jpg")
        self.floor=self.createSprite(0,self.wall_l.rect.bottom-3,"level3/floor.jpg")
        self.button_sound=self.createSprite(10,10,"level1/sound.jpg")
        self.List1=self.crearCirculos(50,100)
        self.List2=self.crearCirculos(650,100)
    
    def crearCirculos(self,x,y):
        num=0
        List=[]
        while (num<4):
            c1=self.createSprite(x, y,"level3/circulo_blanco.png")
            List.append(c1)
            c2=self.createSprite(x+100, y,"level3/circulo_blanco.png")
            List.append(c2)
            y=y+90
            num=num+1
        return List
        
    def checkMoveDoor(self,patron,patron2):
        #print patron[1:8]
        #print patron2[1:8]
        resolucion1=["1","0","0","1","1","0","0","1"]
        resolucion2=["0","1","1","0","0","1","1","0"]
        if(patron==resolucion1 and patron2==resolucion2):
            vx=-1
            vy=0
            self.door_l.rect.move_ip(vx,vy)
            self.door_r.rect.move_ip(-vx,vy)

            