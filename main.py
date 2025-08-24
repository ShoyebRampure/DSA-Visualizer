import pygame, sys
from Buttons import Button
from Menu import *

from UIProperties import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock  = pygame.time.Clock()
Icon = pygame.image.load("ICON.jpg")
pygame.display.set_icon(Icon)
Menu_Btns= []
Sel_Btns=[]
menu_b1 = Button(230, 150, r'B_Pink.png', "START", 48,320, 160)
menu_b2 = Button(230, 270, r'B_DedBlu.png', "SETTINGS", 48,320, 160)
menu_b3 = Button(230, 390, r'B_Purp.png', "QUIT", 48,320, 160)
menu_b4 = Button(120, 150, r'B_Green.png', "Data Structures", 48,480, 240)
menu_b5 = Button(120, 350, r'B_Maroon.png', "Algorithms", 48,480, 240)
Menu_Btns.append(menu_b1)
Menu_Btns.append(menu_b2)
Menu_Btns.append(menu_b3)
Sel_Btns.append(menu_b4)
Sel_Btns.append(menu_b5)
menu = MenuObj(screen, clock, 800, 600, Menu_Btns, Sel_Btns)
pygame.display.set_caption("Algorithm Visulaizer")
menu_Dict={'START':menu.SelectionButtons_Display }

menu.title_screen()


while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        menu.HandleEvents(event)
        
    
    menu.HandleDisplay()
    
    
    pygame.display.flip()
    clock.tick(60)
