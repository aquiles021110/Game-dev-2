import pgzrun,random
TITLE='boing'
WIDTH=800
HEIGHT=500
gravity=2000
class ball:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    self.vx=200
    self.vy=0
    self.radius=40
  def draw(self):
    screen.draw.filled_circle((self.x,self.y),self.radius,'red')
b1=ball(40,250)    
def draw():
  screen.clear()
  b1.draw()
def update(t):
  uy=b1.vy
  b1.vy+=gravity*t
  b1.y+=(uy+b1.vy)*0.5*t
  if b1.y>HEIGHT-b1.radius:
    b1.y=HEIGHT-b1.radius
    b1.vy=-b1.vy*0.9
  b1.x+=b1.vx*t
  if b1.x>WIDTH-b1.radius or b1.x<b1.radius:
    b1.vx=-b1.vx
def on_key_down(key):
  if key==keys.SPACE:
    b1.vy=-500
pgzrun.go()
