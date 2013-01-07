'''
Created on 28/12/2012

@author: Keab
'''
import pygame
pygame.init()


class Level4():
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
    hacha= None
    ventana= None
    hachaSeleccionada=False
    ventana_quebrada=pygame.image.load("level4/ventana_quebrada.jpg")
    patron=["0","0","0","0","0","0","0","0"]
    sound1=pygame.mixer.Sound("level4/acertijo4.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    flag=0
    i=0
    fin=True
    check=False
    
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
        screen.blit(self.ventana.image,self.ventana.rect)
        screen.blit(self.hacha.image,self.hacha.rect)
        screen.blit(self.control.image,self.control.rect)
        screen.blit(self.button_sound.image,self.button_sound.rect)
        screen.blit(self.panel.image,self.panel.rect)
        
        
    def createLevel(self):
        self.wall_u = self.createSprite(0,0,"level4/pared_sup.jpg")
        self.wall_l = self.createSprite(0, self.wall_u.rect.bottom ,"level4/pared_izq.jpg") 
        self.door_l = self.createSprite(self.wall_l.rect.right, self.wall_u.rect.bottom, "level4/puerta_izq.jpg")
        self.door_intern=self.createSprite(self.wall_l.rect.right,self.wall_u.rect.bottom,"level4/puerta_dentro.jpg")
        self.door_r = self.createSprite(self.door_l.rect.right-2, self.wall_u.rect.bottom, "level4/puerta_der.jpg")
        self.wall_r = self.createSprite(self.door_r.rect.right-2, self.wall_u.rect.bottom, "level4/pared_der.jpg")
        self.floor=self.createSprite(0,self.wall_l.rect.bottom,"level4/floor.jpg")
        self.button_sound=self.createSprite(10,10,"level1/sound.jpg")
        self.ventana=self.createSprite(50,110,"level4/ventana.jpg")
        self.control=self.createSprite(180,310,"level4/control.jpg")
        self.hacha=self.createSprite(700,200,"level4/hacha.png")
        self.panel=self.createSprite(860,100,"level4/panel_numeros.jpg")
    
    def checkMoveDoor(self,patron):
        resolucion=["4","1","2","0","0","0","0","0"]
        print patron[0:7]
        if(patron[0:3]==resolucion[0:3]):
            vx=-1
            vy=0
            self.door_l.rect.move_ip(vx,vy)
            self.door_r.rect.move_ip(-vx,vy)
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
        
    def checking(self, screen ):
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
                            patron=["0","0","0","0","0","0","0","0"]
                            self.i=0
                    if(self.hacha.rect.collidepoint(x,y)):
                        if(self.hachaSeleccionada  and self.hacha.rect.colliderect(self.ventana)):
                            self.hachaSeleccionada=True
                            self.ventana.image=self.ventana_quebrada
                        else: 
                            if(self.hachaSeleccionada  and not(self.hacha.rect.colliderect(self.ventana))):
                                self.hachaSeleccionada=False
                            else:
                                self.hachaSeleccionada=True
                    if(self.door_intern.rect.collidepoint(x,y) and self.check):
                        self.fin=False
                    
            c1.tick(60)
            if(self.hachaSeleccionada):
                x,y=pygame.mouse.get_pos()
                x=x-25
                y=y-25
                self.hacha.rect.left,self.hacha.rect.top=x,y
            
            self.checkMoveDoor(self.patron)
            self.moverPanel(self.flag)
            screen.fill((200,200,200))
            self.update(screen)
            pygame.display.update()            