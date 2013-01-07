'''
Created on 07/01/2013

@author: Hernan
'''
import pygame
pygame.init()

class Portada():
    portada=None
    boton=None
    salir=None
    imagen1=pygame.image.load("Portada/boton1.png")
    imagen2=pygame.image.load("Portada/boton2.png")
    imag1=pygame.image.load("Portada/exit1.jpg")
    imag2=pygame.image.load("Portada/exit2.jpg")
    fin=True
    fin2=True
    
    def __init__(self):
        self.createPortada()
        
    def createSprite(self,x,y,adr):
        s1 = pygame.sprite.Sprite()
        s1.image = pygame.image.load(adr).convert_alpha()
        s1.rect = s1.image.get_rect()
        (s1.rect.left, s1.rect.top) = (x,y)
        return s1
    
    def update(self,screen):
        screen.blit(self.portada.image,self.portada.rect)
        screen.blit(self.boton.image,self.boton.rect)
        screen.blit(self.salir.image,self.salir.rect)
        
    def createPortada(self): 
        self.portada=self.createSprite(0,0,"Portada/portada.jpg")
        self.boton=self.createSprite(637, 460,"Portada/boton1.png")
        self.salir=self.createSprite(10,10,"Portada/exit1.jpg")
    
    def checking(self,screen):
        c1 = pygame.time.Clock()
        while (True and self.fin and self.fin2):
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    quit()
                if events.type == pygame.MOUSEMOTION:
                    x,y=pygame.mouse.get_pos()
                    if(self.boton.rect.collidepoint(x,y)):
                        self.boton.image=self.imagen2
                    else:
                        self.boton.image=self.imagen1
                    if(self.salir.rect.collidepoint(x,y)):
                        self.salir.image=self.imag2
                    else:
                        self.salir.image=self.imag1
                if events.type == pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if(self.boton.rect.collidepoint(x,y)):
                        self.fin=False
                    if(self.salir.rect.collidepoint(x,y)):
                        self.fin2=False
                        
            c1.tick(60)
            screen.fill((200,200,200))
            self.update(screen)
            pygame.display.update()