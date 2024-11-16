import pygame.transform
import pygame
pygame.init()
screen=pygame.display.set_mode((1000,600))
#1=yellow 2=red
hp1=10
hp2=10
gameover=False
winner=''
yellow=pygame.transform.rotate(pygame.transform.scale(pygame.image.load('yellow.png'),(50,50)),90)
red=pygame.transform.rotate(pygame.transform.scale(pygame.image.load('red.png'),(50,50)),270)
space=pygame.transform.scale(pygame.image.load('space2.png'),(1000,600))
yellowrect=pygame.Rect(100,300,50,50)
redrect=pygame.Rect(900,300,50,50)
border=pygame.Rect(485,0,30,600)
font=pygame.font.SysFont('Sans Serif',50)
bullety=[]
bulletr=[]
def draw():
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,'black',border)
    healthy=font.render(f'HEALTH:{hp1}',True,'white')
    healthr=font.render(f'HEALTH:{hp2}',True,'white')
    screen.blit(healthr,(800,100))
    screen.blit(healthy,(200,100))
    screen.blit(red,(redrect.x,redrect.y))
    screen.blit(yellow,(yellowrect.x,yellowrect.y))
    gameovrtxt=font.render(f'GAME OVER \n {winner} WON',True,'white')
    if gameover:
        screen.blit(space,(0,0))
        screen.blit(gameovrtxt,(400,250))
    for i in bullety:
        pygame.draw.rect(screen,'yellow',i)
    for i in bulletr:
        pygame.draw.rect(screen,'red',i)
def ymov(keys):
    if keys[pygame.K_w] and yellowrect.y>0:
        yellowrect.y-=1
    if keys[pygame.K_a] and yellowrect.x>0:
        yellowrect.x+=1
    if keys[pygame.K_s] and yellowrect.y<600:
        yellowrect.y+=1
    if keys[pygame.K_d] and yellowrect.x<485:
        yellowrect.x+=1
def rmov(keys):
    if keys[pygame.K_i] and redrect.y>0:
        redrect.y-=1
    if keys[pygame.K_j] and redrect.x>515:
        redrect.x-=1
    if keys[pygame.K_k] and redrect.y<600:
        redrect.y+=1
    if keys[pygame.K_l] and redrect.x<1000:
        redrect.x+=1
def bullet(bullety,bulletr):
    for i in bullety:
        i.x+=3
        if redrect.colliderect(i):
            bullety.remove(i)
            hp2-=1
        elif i.x>1000:
            bullety.remove(i)
    for i in bulletr:
        i.x-=3
        if redrect.colliderect(i):
            bulletr.remove(i)
            hp1-=1
        elif i.x<0:
            bulletr.remove(i)
def gover():
    global winner,gameover
    if hp1==0:
        winner='RED'
        gameover=True
    elif hp2==0:
        winner='YELLOW'
        gameover=True
