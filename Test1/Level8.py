'''
Created on 03/01/2013

@author: Hernan
'''
import pygame
pygame.init()


#Octavo Nivel.- 
class Level8():
    button_sound=None
    wall_r = None
    wall_l = None
    wall_u = None
    floor= None
    door_l = None
    door_r = None
    door_intern= None
    lampara1=None
    lampara2=None
    lampara3=None
    lampara4=None
    sound1=pygame.mixer.Sound("level8/acertijo8.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    lampara1select=False
    lampara2select=False
    lampara3select=False
    lampara4select=False
    fin=True
    check=False
    
	#metodo constructor
    def __init__(self):
        self.createLevel()
        
                
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1
    
	#Actualizacion de todos los elementos del Nivel
    def update(self,screen):
        screen.blit(self.door_intern.image,self.door_intern.rect)
        screen.blit(self.door_l.image,self.door_l.rect)
        screen.blit(self.wall_l.image,self.wall_l.rect)
        screen.blit(self.wall_r.image,self.wall_r.rect)
        screen.blit(self.floor.image,self.floor.rect)
        screen.blit(self.wall_u.image,self.wall_u.rect)
        screen.blit(self.button_sound.image,self.button_sound.rect)
        screen.blit(self.lampara1.image,self.lampara1.rect)
        screen.blit(self.lampara2.image,self.lampara2.rect)
        screen.blit(self.lampara3.image,self.lampara3.rect)
        screen.blit(self.lampara4.image,self.lampara4.rect)
        
	
        #Cargamos todos los elementos del Nivel
    def createLevel(self):
        self.wall_u = self.createSprite(0,0,"level8/pared_sup.jpg")
        self.wall_l = self.createSprite(0, self.wall_u.rect.bottom ,"level8/pared_izq.jpg") 
        self.door_l = self.createSprite(self.wall_l.rect.right, self.wall_u.rect.bottom, "level8/puerta.jpg")
        self.door_intern=self.createSprite(self.wall_l.rect.right,self.wall_u.rect.bottom,"level8/puerta_dentro.jpg")
        self.wall_r = self.createSprite(self.door_l.rect.right-3, self.wall_u.rect.bottom-3, "level8/pared_der.jpg")
        self.floor=self.createSprite(0,self.wall_l.rect.bottom-4,"level8/floor.jpg")
        self.button_sound=self.createSprite(10,10,"level1/sound.jpg")
        self.lampara1=self.createSprite(40,-180,"level8/lampara.png")
        self.lampara2=self.createSprite(180,-180,"level8/lampara.png")
        self.lampara3=self.createSprite(570,-180,"level8/lampara.png")
        self.lampara4=self.createSprite(690,-180,"level8/lampara.png")
    
	#Se controla la Solucion del Nivel
    def checkLamparas(self,l1,l2,l3,l4):
        encendida=pygame.image.load("level8/lampara2.png")
        apagada=pygame.image.load("level8/lampara.png")
        flag1,flag2,flag3,flag4=False,False,False,False
        if(l1==180):
            self.lampara1.image=encendida
            flag1=True
        else:
            self.lampara1.image=apagada
        if(l2==130):
            self.lampara2.image=encendida
            flag2=True
        else:
            self.lampara2.image=apagada
        if(l3==225):
            self.lampara3.image=encendida
            flag3=True
        else:
            self.lampara3.image=apagada
        if(l4==80):
            self.lampara4.image=encendida
            flag4=True
        else:
            self.lampara4.image=apagada
        if(flag1 and flag2 and flag3 and flag4):
            return 1
        else:
            return 0
    def checkMoveDoor(self,solucion):
        if(solucion):
            vx=-1
            vy=0
            self.door_l.rect.move_ip(vx,vy)
            self.check=True
            
    def checking(self,screen):
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
                    if(self.lampara1.rect.collidepoint(x,y)):
                        if(self.lampara1select):
                            self.lampara1select=False
                        else:
                            self.lampara1select=True
                    if(self.lampara2.rect.collidepoint(x,y)):
                        if(self.lampara2select):
                            self.lampara2select=False
                        else:
                            self.lampara2select=True
                    if(self.lampara3.rect.collidepoint(x,y)):
                        if(self.lampara3select):
                            self.lampara3select=False
                        else:
                            self.lampara3select=True
                    if(self.lampara4.rect.collidepoint(x,y)):
                        if(self.lampara4select):
                            self.lampara4select=False
                        else:
                            self.lampara4select=True
            c1.tick(60)
            x,y=pygame.mouse.get_pos()
            y=y+30
            if(self.lampara1select and self.lampara1.rect.top<0):
                self.lampara1.rect.bottom=y
            if(self.lampara1.rect.top>=0):
                self.lampara1.rect.top=-2
            if(self.lampara2select and self.lampara2.rect.top<0):
                self.lampara2.rect.bottom=y
            if(self.lampara2.rect.top>=0):
                self.lampara2.rect.top=-2
            if(self.lampara3select and self.lampara3.rect.top<0):
                self.lampara3.rect.bottom=y
            if(self.lampara3.rect.top>=0):
                self.lampara3.rect.top=-2
            if(self.lampara4select and self.lampara4.rect.top<0):
                self.lampara4.rect.bottom=y
            if(self.lampara4.rect.top>=0):
                self.lampara4.rect.top=-2
            solucion=self.checkLamparas(self.lampara1.rect.bottom,self.lampara2.rect.bottom,self.lampara3.rect.bottom,self.lampara4.rect.bottom)
            self.checkMoveDoor(solucion)
            screen.fill((200,200,200))
            self.update(screen)
            pygame.display.update()
            pygame.display.flip()
