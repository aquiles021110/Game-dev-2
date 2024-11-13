import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,600))
score=0
class blocks(pygame.sprite.Sprite):
  def __init__(self,colour):
    super().__init__()
    self.image=pygame.Surface((20,30))
    self.image.fill(colour)
    self.rect=self.image.get_rect()
black_blocks=pygame.sprite.Group()
all=pygame.sprite.Group()
for i in range(50):
  bblock=blocks('black')
  bblock.rect.x=random.randrange(800)
  bblock.rect.y=random.randrange(600)
  black_blocks.add(bblock)
  all.add(bblock)
bred=blocks('red')
all.add(bred)
while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      exit()
  screen.fill('white')
  pos=pygame.mouse.get_pos()
  bred.rect.x=pos[0]
  bred.rect.y=pos[1]
  hit=pygame.sprite.spritecollide(bred,black_blocks,True)
  for i in hit:
    score+=1
    print(score)
  all.draw(screen)
  pygame.display.update()
