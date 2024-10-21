import time
import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('Card')
while True:
    v2=pygame.image.load('note.jpg')
    '''v1=pygame.transform.scale(v1,(1000,1000))'''
    font=pygame.font.SysFont('Comic Sans',60)
    textv2=font.render('Wow, many age',True,'Black')
    screen.blit(v2,(0,0))
    screen.blit(textv2,(150,230))
    pygame.display.update()
    time.sleep(2)
    v3=pygame.image.load('present.jpg')
    '''v1=pygame.transform.scale(v1,(1000,1000))'''
    font=pygame.font.SysFont('Arial',60)
    textv3=font.render('Omg a present',True,'Red')
    screen.blit(v3,(0,0))
    screen.blit(textv3,(150,100))
    pygame.display.update()
    time.sleep(2)
    v1=pygame.image.load('cake.jpg')
    '''v1=pygame.transform.scale(v1,(1000,1000))'''
    font=pygame.font.SysFont('Montersserat',60)
    textv1=font.render('Happy Birthday',True,'Black')
    screen.blit(v1,(0,0))
    screen.blit(textv1,(150,80))
    pygame.display.update()
    time.sleep(2)
    
