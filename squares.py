import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
class Rect:
    def __init__(self,colour,dimensions):
        self.screen=screen
        self.colour=colour
        self.dimensions=dimensions
    def draw(self):
        self.draw_rect=pygame.draw.rect(self.screen,self.colour,self.dimensions)
rect1=Rect('red',(100,100,200,200))
rect2=Rect('green',(300,350,400,450))
rect3=Rect('blue',(50,400,150,500))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill('white')
    rect1.draw()
    rect2.draw()
    rect3.draw()
    pygame.display.update()
    
