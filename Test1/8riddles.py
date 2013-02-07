'''
Created on 24/12/2012

@author: Hernan
'''
#Todos los levels son creados como clases donde son incializados todos sus recursos
#Debido a esto se importan cada clase de su respectivo level

import pygame
from Level1 import Level1 
from Level2 import Level2
from Level3 import Level3
from Level4 import Level4
from Level5 import Level5
from Level6 import Level6
from Level7 import Level7
from Level8 import Level8
from Portada import Portada

def main():
    #Caracteristicas de la Ventana
    pygame.init()
    icon=pygame.image.load("icon.png")
    screen = pygame.display.set_mode((860,578))
    pygame.display.set_caption("8 RIDDLES")
    pygame.display.set_icon(icon)
    
    
    p=Portada()
    l1 = Level1()
    l2 = Level2()
    l3 = Level3()
    l4 = Level4()
    l5 = Level5()
    l6 = Level6()
    l7 = Level7()
    l8 = Level8()
    
    p.checking(screen)
    l1.checking(screen)
    l2.checking(screen)
    l3.checking(screen)    
    l4.checking(screen) 
    l5.checking(screen)
    l6.checking(screen)
    l7.checking(screen)
    l8.checking(screen)
        
    
main()



