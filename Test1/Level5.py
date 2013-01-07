'''
Created on 29/12/2012

@author: Hernan
'''
import pygame
pygame.init()


class Level5():
    button_sound=None
    wall_r = None
    wall_l = None
    wall_u = None
    floor= None
    door_l = None
    door_r = None
    door_intern= None
    patron=[]
    fin=True
    check=False
    sound1=pygame.mixer.Sound("level5/acertijo5.wav")
    door_izq=pygame.mixer.Sound("level5/door_izq.wav")
    door_der=pygame.mixer.Sound("level5/door_der.wav")
    pygame.mixer_music.load("level1/elevador.mp3")
    i=0
    
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
        
        
    def createLevel(self):
        self.wall_u = self.createSprite(0,0,"level5/pared_sup.jpg")
        self.wall_l = self.createSprite(0, self.wall_u.rect.bottom ,"level5/pared_izq.jpg") 
        self.door_l = self.createSprite(self.wall_l.rect.right, self.wall_u.rect.bottom, "level5/puerta_izq.jpg")
        self.door_intern=self.createSprite(self.wall_l.rect.right,self.wall_u.rect.bottom,"level5/puerta_dentro.jpg")
        self.door_r = self.createSprite(self.door_l.rect.right, self.wall_u.rect.bottom, "level5/puerta_der.jpg")
        self.wall_r = self.createSprite(self.door_r.rect.right, self.wall_u.rect.bottom, "level5/pared_der.jpg")
        self.floor=self.createSprite(0,self.wall_l.rect.bottom-3,"level5/floor.jpg")
        self.button_sound=self.createSprite(10,10,"level1/sound.jpg")
    
    def checkMoveDoor(self,patron):
        solucion=["1","2","1","1","1","2"]
        if(patron==solucion):
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
                    if(self.door_l.rect.collidepoint(x,y)):
                        self.door_izq.play()
                        self.patron.append("1")
                        if(self.i<6):
                            self.i=self.i+1
                        else: 
                            self.i=0
                            self.patron=[]
                            self.patron.append("1")
                    if(self.door_r.rect.collidepoint(x,y)):
                        self.door_der.play()
                        self.patron.append("2")
                        if(self.i<6):
                            self.i=self.i+1
                        else: 
                            self.i=0
                            self.patron=[]
                            self.patron.append("2")
                    if(self.button_sound.rect.collidepoint(x,y)):
                        self.sound1.play()
                        
                    if(self.door_intern.rect.collidepoint(x,y) and self.check):
                        self.fin=False
                        
            
            c1.tick(60)
            self.checkMoveDoor(self.patron)
            screen.fill((200,200,200))
            self.update(screen)
            pygame.display.update()
