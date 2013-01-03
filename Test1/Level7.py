'''
Created on 02/01/2013

@author: Hernan
'''
import pygame


class Level7():
    button_sound=None
    wall_r = None
    wall_l = None
    wall_u = None
    floor= None
    door_l = None
    door_r = None
    door_intern= None
    raton=None
    snake=None
    control= None
    panel= None
    plato1=None
    plato2=None
    plato3=None
    
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
        screen.blit(self.control.image,self.control.rect)
        screen.blit(self.panel.image,self.panel.rect)
        screen.blit(self.plato1.image,self.plato1.rect)
        screen.blit(self.plato2.image,self.plato2.rect)
        screen.blit(self.plato3.image,self.plato3.rect)
        screen.blit(self.snake.image,self.snake.rect)
        screen.blit(self.raton.image,self.raton.rect)
        
        
    def createLevel(self):
        self.wall_u = self.createSprite(0,0,"level7/pared_sup.jpg")
        self.wall_l = self.createSprite(0, self.wall_u.rect.bottom ,"level7/pared_izq.jpg") 
        self.door_l = self.createSprite(self.wall_l.rect.right, self.wall_u.rect.bottom, "level7/puerta_izq.jpg")
        #self.door_intern=self.createSprite(self.wall_l.rect.right,self.wall_u.rect.bottom,"level5/puerta_dentro.jpg")
        self.door_r = self.createSprite(self.door_l.rect.right, self.wall_u.rect.bottom, "level7/puerta_der.jpg")
        self.wall_r = self.createSprite(self.door_r.rect.right-6, self.wall_u.rect.bottom, "level7/pared_der.jpg")
        self.floor=self.createSprite(0,self.wall_l.rect.bottom-3,"level7/floor.jpg")
        
        self.raton=self.createSprite(-68, self.floor.rect.top,"level7/raton.png")
        
        self.control=self.createSprite(270,270,"level7/control.jpg")
        self.panel=self.createSprite(860,100,"level7/panel_numeros.jpg")
        self.button_sound=self.createSprite(10,10,"level1/sound.jpg")
        self.snake=self.createSprite(860,8,"level7/snake.png")
        self.plato1=self.createSprite(650,12,"level7/plato.png")
        self.plato2=self.createSprite(450,12,"level7/plato.png")
        self.plato3=self.createSprite(250,12,"level7/plato.png")
    
    def checkMoveDoor(self,patron):
        resolucion=["6","1","8","0","0","0","0","0"]
        if(patron[0:3]==resolucion[0:3]):
            vx=-1
            vy=0
            self.door_l.rect.move_ip(vx,vy)
            self.door_r.rect.move_ip(-vx,vy)
    
    def moverRaton(self):
        if(self.raton.rect.left<860):
            vx=5
            vy=0
            self.raton.rect.move_ip(vx,vy)
        else:
            self.raton.rect.left,self.raton.rect.top=-68,self.floor.rect.top
    
    def moverPanel(self,flag):
        if(flag==1):
            vx=-3
            vy=0
            if(self.panel.rect.left>=550):
                self.panel.rect.move_ip(vx,vy)
        else:
            vx=3
            vy=0
            if(self.panel.rect.left<=860):
                self.panel.rect.move_ip(vx,vy)
