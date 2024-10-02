import pygame
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('Drawing')
class circles:
  def __init__(self,colour,pos,radius):
    self.colour=colour
    self.pos=pos
    self.radius=radius
    self.screen=screen
  def draw(self):
    pygame.draw.circle(self.screen,self.colour,self.pos,self.radius)
  def grow(self,x):
    self.radius+=x
    pygame.draw.circle(self.screen,self.colour,self.pos,self.radius)
pygame.display.update()
circle1=circles('red',(400,400),40)
circle2=circles('green',(400,400),60)
circle3=circles('blue',(400,400),80)
while True:
  screen.fill('white')
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
      circle1.draw()
      circle2.draw()
      circle3.draw()
      pygame.display.update()
    elif event.type==pygame.MOUSEBUTTONUP:
      circle1.grow(10)
      circle2.grow(10)
      circle3.grow(10)
      pygame.display.update()
    elif event.type==pygame.MOUSEMOTION:
      pos=pygame.mouse.get_pos()
      circledraw=circles('black',(pos),10)
      circledraw.draw()
      pygame.display.update()
