# Write your code here :-)
import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill('White')
pygame.display.set_caption('Painting')
colours=['red','green','blue','black','white','orange','purple']
drawing=False
startpos=None
currentcolour='black'
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            drawing=True
            startpos=event.pos()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            drawing=False
            pygame.display.update()
        elif event.type==pygame.MOUSEMOTION:
            if drawing:
                currentpos=event.pos
                pygame.draw.line(screen,currentcolour,startpos,currentpos)
                startpos=currentpos
                pygame.display.update()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e:
                colourpick=random.choice(colours)
                currentcolour=colourpick
pygame.display.update()
