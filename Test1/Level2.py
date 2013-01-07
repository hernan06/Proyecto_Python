'''
Created on 26/12/2012

@author: Hernan
'''
import pygame
pygame.init()

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
    fin=True
    check=False
    sound1=pygame.mixer.Sound("level2/acertijo2.wav")
    sound2=pygame.mixer.Sound("level2/puerta.wav")
    ball1_selected=False
    ball2_selected=False

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
        self.door_intern=self.createSprite(229, self.wall_u.rect.bottom,"level2/puerta_dentro.jpg")
        self.button_sound=self.createSprite(10,10,"level1/sound.jpg")
        self.ball1=self.createSprite(self.wall_l1.rect.right,self.floor.rect.top-42,"level2/esfera.jpg")
        self.ball2=self.createSprite(self.wall_r1.rect.right,self.wall_u.rect.bottom+2,"level2/esfera.jpg")
        
        
    def checkMoveDoor(self,altura1,altura2):
        if(altura1>=180 and altura1<=224 and altura2>=375 and altura2<=424):
            vx=-1
            vy=0
            self.door_l.rect.move_ip(vx,vy)
            self.door_r.rect.move_ip(-vx,vy)
            self.check=True
            
            
    def checking(self, screen):
        c1 = pygame.time.Clock()
        f=True
        while (True and self.fin):
            (x,y)=(0,0)
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.button_sound.rect.collidepoint( x, y)):
                        self.sound1.play()
                    if(self.ball1.rect.collidepoint(x,y) and not(self.ball2_selected)):
                        if(self.ball1_selected):
                            self.ball1_selected=False
                        else:
                            self.ball1_selected=True
                    if(self.ball2.rect.collidepoint(x,y) and not(self.ball1_selected)):
                        if(self.ball2_selected):
                            self.ball2_selected=False
                        else:
                            self.ball2_selected=True
                    if(self.door_intern.rect.collidepoint(x,y) and self.check):
                        self.fin=False
                
            oldy=self.ball1.rect.top
            oldy2=self.ball2.rect.top
            if(self.ball1_selected):
                x,y=pygame.mouse.get_pos()
                self.ball1.rect.top=y
                if(self.ball1.rect.colliderect(self.wall_u.rect) or self.ball1.rect.colliderect(self.floor.rect)):
                    self.ball1.rect.top=oldy
            if(self.ball2_selected):
                x,y=pygame.mouse.get_pos()
                self.ball2.rect.top=y
                if(self.ball2.rect.colliderect(self.wall_u.rect) or self.ball2.rect.colliderect(self.floor.rect)):
                    self.ball2.rect.top=oldy2
            c1.tick(30)    
            self.checkMoveDoor(self.ball1.rect.top,self.ball2.rect.top)
            screen.fill((255,255,255))
            self.update(screen)
            pygame.display.update()
        