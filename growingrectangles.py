import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill('light blue')
pygame.display.update()
#init function is to intialize everything

class Grow():
    def __init__(self,color,pos,height,width):
        self.color=color
        self.pos=pos
        self.height=height
        self.width=width
        self.surface=screen
#init function is to initialize everything
#this function helps with the charecteristics of the rectangle

    def draw(self):
        pygame.draw.rect(self.surface,self.color,(self.pos[0],self.pos[1],self.width,self.height))
#this function will simply draw the rectangle

    def growrectangle(self,x,y):
        self.height=self.height+y
        self.width=self.width+x
        self.draw()
#grow rectangle helps grow the height of the rectangle

redrectangle=Grow('red',(50,50),30,100)

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
#whenever you close the screen completely it will automatically quit the game

        if i.type==pygame.MOUSEBUTTONDOWN:
            screen.fill('light pink')
            redrectangle.draw()
            pygame.display.update()
#this is when you click the mouse it simply draws the rectangle

        if i.type==pygame.MOUSEBUTTONUP:
            screen.fill('light pink')
            redrectangle.growrectangle(10,10)
            pygame.display.update()
#when you release the mouse button the rectangle gets bigger

    pygame.display.update()