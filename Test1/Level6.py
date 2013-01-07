'''
Created on 31/12/2012

@author: Keab
'''
import pygame
pygame.init()

class Level6():
    button_sound=None
    wall_r = None
    wall_l = None
    wall_u = None
    floor= None
    door_l = None
    door_r = None
    door_intern= None
    control= None
    panel= None
    cono1=None
    cono2=None
    toma=None
    muro1=None
    muro2=None
    fin=True
    check=False
    patron=["0","0","0","0","0","0","0","0"]
    sound1=pygame.mixer.Sound("level6/acertijo6.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    i=0
    flag=0
    cono1_seleccionado=False
    cono2_seleccionado=False
    toma_seleccionado=False
    muro1_seleccionado=False
    muro2_seleccionado=False
    
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
        screen.blit(self.wall_l.image,self.wall_l.rect)
        screen.blit(self.wall_r.image,self.wall_r.rect)
        screen.blit(self.floor.image,self.floor.rect)
        screen.blit(self.wall_u.image,self.wall_u.rect)
        screen.blit(self.control.image,self.control.rect)
        screen.blit(self.button_sound.image,self.button_sound.rect)
        screen.blit(self.panel.image,self.panel.rect)
        screen.blit(self.cono1.image,self.cono1.rect)
        screen.blit(self.cono2.image,self.cono2.rect)
        screen.blit(self.muro1.image,self.muro1.rect)
        screen.blit(self.muro2.image,self.muro2.rect)
        screen.blit(self.toma.image,self.toma.rect)
        
    def createLevel(self):
        self.wall_u = self.createSprite(0,0,"level6/pared_sup.jpg")
        self.wall_l = self.createSprite(0, self.wall_u.rect.bottom ,"level6/pared_izq.jpg") 
        self.door_l = self.createSprite(self.wall_l.rect.right, self.wall_u.rect.bottom, "level6/puerta.jpg")
        self.door_intern=self.createSprite(self.wall_l.rect.right,self.wall_u.rect.bottom,"level6/puerta_dentro.jpg")
        self.wall_r = self.createSprite(self.door_l.rect.right, self.wall_u.rect.bottom, "level6/pared_der.jpg")
        self.floor=self.createSprite(0,self.wall_l.rect.bottom-3,"level6/floor.jpg")
        self.control=self.createSprite(130,250,"level6/control.jpg")
        self.button_sound=self.createSprite(10,10,"level1/sound.jpg")
        self.panel=self.createSprite(860,100,"level6/panel_numeros.jpg")
        self.toma=self.createSprite(30,self.floor.rect.top,"level6/toma.png")
        self.cono1=self.createSprite(self.toma.rect.right+100,self.floor.rect.top,"level6/cono_parado.png")
        self.muro1=self.createSprite(self.cono1.rect.right+110,self.floor.rect.top,"level6/muro.png")
        self.muro2=self.createSprite(self.muro1.rect.right+100,self.floor.rect.top,"level6/muro2.png")
        self.cono2=self.createSprite(self.muro2.rect.right,self.floor.rect.top+50,"level6/cono_parado2.png")
        
        
    
    def checkMoveDoor(self,patron):
        solucion=["2","3","1","9","0","0","0","0"]
        if(patron[0:4]==solucion[0:4]):
            vx=0
            vy=-1
            self.door_l.rect.move_ip(vx,vy)
            self.check=True
            
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
    
    def checking(self,screen):
        c1 = pygame.time.Clock()
        while True and self.fin:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.KEYDOWN:
                    if(self.flag==1 and events.key == pygame.K_1):
                        self.patron.pop(self.i)
                        self.patron.insert(self.i,"1")
                        if(self.i<7):
                            self.i=self.i+1
                    if(self.flag==1 and events.key == pygame.K_2):
                        self.patron.pop(self.i)
                        self.patron.insert(self.i,"2")
                        if(self.i<7):
                            self.i=self.i+1
                    if(self.flag==1 and events.key == pygame.K_3):
                        self.patron.pop(self.i)
                        self.patron.insert(self.i,"3")
                        if(self.i<7):
                            self.i=self.i+1
                    if(self.flag==1 and events.key == pygame.K_4):
                        self.patron.pop(self.i)
                        self.patron.insert(self.i,"4")
                        if(self.i<7):
                            self.i=self.i+1
                    if(self.flag==1 and events.key == pygame.K_5):
                        self.patron.pop(self.i)
                        self.patron.insert(self.i,"5")
                        if(self.i<7):
                            self.i=self.i+1
                    if(self.flag==1 and events.key == pygame.K_6):
                        self.patron.pop(self.i)
                        self.patron.insert(self.i,"6")
                        if(self.i<7):
                            self.i=self.i+1
                    if(self.flag==1 and events.key == pygame.K_7):
                        self.patron.pop(self.i)
                        self.patron.insert(self.i,"7")
                        if(self.i<7):
                            self.i=self.i+1
                    if(self.flag==1 and events.key == pygame.K_8):
                        self.patron.pop(self.i)
                        self.patron.insert(self.i,"8")
                        if(self.i<7):
                            self.i=self.i+1
                    if(self.flag==1 and events.key == pygame.K_9):
                        self.patron.pop(self.i)
                        self.patron.insert(self.i,"9") 
                        if(self.i<7):
                            self.i=self.i+1   
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_sound.rect.collidepoint( x, y)):
                        self.sound1.play()
                    if(self.control.rect.collidepoint(x,y)):
                        if(self.flag==0):
                            self.flag=1
                        else: 
                            self.flag=0
                            self.patron=["0","0","0","0","0","0","0","0"]
                            self.i=0
                    if(self.cono1.rect.collidepoint(x,y)):
                        if(not(self.cono1_seleccionado)):
                            self.cono1_seleccionado=True
                        else:
                            self.cono1_seleccionado=False
                    if(self.cono2.rect.collidepoint(x,y)):
                        if(not(self.cono2_seleccionado)):
                            self.cono2_seleccionado=True
                        else:
                            self.cono2_seleccionado=False
                    if(self.muro1.rect.collidepoint(x,y)):
                        if(not(self.muro1_seleccionado)):
                            self.muro1_seleccionado=True
                        else:
                            self.muro1_seleccionado=False
                    if(self.muro2.rect.collidepoint(x,y)):
                        if(not(self.muro2_seleccionado)):
                            self.muro2_seleccionado=True
                        else:
                            self.muro2_seleccionado=False
                    if(self.toma.rect.collidepoint(x,y)):
                        if(not(self.toma_seleccionado)):
                            self.toma_seleccionado=True
                        else:
                            self.toma_seleccionado=False
                    if(self.door_intern.rect.collidepoint(x,y) and self.check):
                        self.fin=False  
            
            c1.tick(60)
            if(self.cono1_seleccionado):
                x,y=pygame.mouse.get_pos()
                x=x-25
                y=y-25
                self.cono1.rect.left,self.cono1.rect.top=x,y
            if(self.cono2_seleccionado):
                x,y=pygame.mouse.get_pos()
                x=x-25
                y=y-25
                self.cono2.rect.left,self.cono2.rect.top=x,y
            if(self.muro1_seleccionado):
                x,y=pygame.mouse.get_pos()
                x=x-25
                y=y-25
                self.muro1.rect.left,self.muro1.rect.top=x,y
            if(self.muro2_seleccionado):
                x,y=pygame.mouse.get_pos()
                x=x-25
                y=y-25
                self.muro2.rect.left,self.muro2.rect.top=x,y
            if(self.toma_seleccionado):
                x,y=pygame.mouse.get_pos()
                x=x-25
                y=y-25
                self.toma.rect.left,self.toma.rect.top=x,y
            self.checkMoveDoor(self.patron)
            self.moverPanel(self.flag)
            screen.fill((200,200,200))
            self.update(screen)
            pygame.display.update()
            pygame.display.flip()
