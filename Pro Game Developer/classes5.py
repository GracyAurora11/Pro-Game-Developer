import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))

class Rectangle:
    def __init__(self,color,dimensions,width,thickness):
        self.color=color
        self.dimensions=dimensions
        self.width=width
        self.thickness=thickness
    
    def display(self):
        pygame.draw.rect(screen,self.color,self.dimensions,self.width,self.thickness)

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
    screen.fill('light blue')
    object1=Rectangle('Blue',(20,20,40,60),100,10)
    object1.display()
    pygame.display.update()