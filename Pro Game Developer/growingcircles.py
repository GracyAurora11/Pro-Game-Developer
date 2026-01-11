import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill('light pink')
pygame.display.update()
#init function is to intialize everything

class Grow():
    def __init__(self,color,pos,radius,width):
        self.color=color
        self.pos=pos
        self.radius=radius
        self.width=width
        self.surface=screen
#init function is to initialize everything
#this function helps with the charecteristics of the circle

    def draw(self):
        pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)
#this function will simply draw the circle

    def growcircle(self,r):
        self.radius=self.radius+r
        pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)
#grow circle helps grow the radius of the circle

greencircle=Grow('green',(200,200),30,0)

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
#whenever you close the screen completely it will automatically quit the game

        if i.type==pygame.MOUSEBUTTONDOWN:
            screen.fill('light pink')
            greencircle.draw()
            pygame.display.update()
#this is when you click the mouse it simply draws the circle

        if i.type==pygame.MOUSEBUTTONUP:
            screen.fill('light pink')
            greencircle.growcircle(10)
            pygame.display.update()
#when you release the mouse button the circle gets bigger

        if i.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            redcircle=Grow('red',pos,5,0)
            redcircle.draw()
            pygame.display.update()
            
