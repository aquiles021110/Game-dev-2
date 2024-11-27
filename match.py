import pygame
pygame.init()
screen=pygame.display.set_mode((1000,600))
screen.fill('white')
candy=pygame.transform.scale(pygame.image.load('candycrush.jpg'),(80,80))
ludo=pygame.transform.scale(pygame.image.load('ludo.png'),(80,80))
subway=pygame.transform.scale(pygame.image.load('subwaysurfers.png'),(80,80))
tombraider=pygame.transform.scale(pygame.image.load('tombraider.png'),(80,80))
font=pygame.font.SysFont('Arial',50)
tombraidertxt=font.render('Tombraider',True,'black')
subwaytxt=font.render('Subway Surfers',True,'black')
ludotxt=font.render('Ludo',True,'black')
candytxt=font.render('Candy Chrush',True,'black')
screen.blit(candy,(300,100))
screen.blit(ludo,(300,200))
screen.blit(subway,(300,300))
screen.blit(tombraider,(300,400))
screen.blit(tombraidertxt,(600,300))
screen.blit(subwaytxt,(600,100))
screen.blit(ludotxt,(600,400))
screen.blit(candytxt,(600,200))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos() 
            pygame.draw.circle(screen,'black',pos,10,0)
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()
            pygame.draw.line(screen,'black',pos,pos2,5)
            pygame.draw.circle(screen,'black',pos2,10,0)
            pygame.display.update()
