'''
Created on 27/12/2012

@author: Hernan
'''
import pygame
pygame.init()


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
    fin=True
    check=False
    sound1=pygame.mixer.Sound("level3/acertijo3.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    blanco=pygame.image.load("level3/circulo_blanco.png")
    rojo=pygame.image.load("level3/circulo_rojo.png")
    patron=["0","0","0","0","0","0","0","0"]
    patron2=["0","0","0","0","0","0","0","0"]

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
        resolucion1=["1","0","0","1","1","0","0","1"]
        resolucion2=["0","1","1","0","0","1","1","0"]
        if(patron==resolucion1 and patron2==resolucion2):
            vx=-1
            vy=0
            self.door_l.rect.move_ip(vx,vy)
            self.door_r.rect.move_ip(-vx,vy)
            self.check=True

            
    def checking(self, screen):
        c1 = pygame.time.Clock()
        
        while True and self.fin:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_sound.rect.collidepoint( x, y)):
                        self.sound1.play()
                    if(self.door_intern.rect.collidepoint(x,y) and self.check):
                        self.fin=False
                    for circle in self.List1:
                        if(circle.rect.collidepoint(x,y)):
                            i=self.List1.index(circle)
                            print i
                            if(circle.image==self.blanco):
                                circle.image=self.rojo
                                self.patron.pop(i)
                                self.patron.insert(i,"1")
                                print self.patron[0:8]
                            else: 
                                circle.image=self.blanco
                                self.patron.pop(i)
                                self.patron.insert(i,"0")
                                print self.patron[0:8]
                                
                    for circle2 in self.List2:
                        if(circle2.rect.collidepoint(x,y)):
                            i= self.List2.index(circle2)
                            if(circle2.image==self.blanco):
                                circle2.image=self.rojo
                                self.patron2.pop(i)
                                self.patron2.insert(i,"1")
                            else: 
                                circle2.image=self.blanco
                                self.patron2.pop(i)
                                self.patron2.insert(i,"0")
                        
            c1.tick(60)
            self.checkMoveDoor(self.patron,self.patron2)
            screen.fill((200,200,200))
            self.update(screen)
            pygame.display.update()