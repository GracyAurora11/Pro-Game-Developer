import pygame, time
pygame.init()
pygame.mixer.init()
#this mixer library is for the music
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#this sets the width and height of the screen

image1=pygame.image.load('Object Orientated Programming/Mothers Day Card/bear.webp')
pygame.display.set_caption('!Happy Mothers Day!')

song=pygame.mixer.Sound('Object Orientated Programming/Mothers Day Card/Maahi.mp3')

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
    font=pygame.font.SysFont('Arial',25)
    text1=font.render('You have been the best mother to me over all these years',True,'light pink')
    screen.fill('light green')
    screen.blit(image1,(0,0))
    screen.blit(text1,(10,75))

    song.play()

    pygame.display.update()
#this is the first image and the first text,font size, type and message to be displayed on the screen

    time.sleep(4)
#this is for how many seconds to wait for when the picture is changing in between the animation

    image2=pygame.image.load('Object Orientated Programming/Mothers Day Card/Roses.jpg')
    font2=pygame.font.SysFont('Arial',27)
    text2=font2.render('Make sure you have a great day with friends and family!',True,'light blue')
    screen.fill('light green')
    screen.blit(image2,(0,0))
#blit is a function to display anything on the screen

    screen.blit(text2,(10,75))
    pygame.display.update()
#this is the second image and the second text,font size,type and message to be displayed on the screen

    time.sleep(4)
#this is for how many seconds to wait for when the picture is changing in between the animation

    image3=pygame.image.load('Object Orientated Programming\Mothers Day Card\Hearts.jpg')
    font3=pygame.font.SysFont('Arial',50)
    text3=font3.render('Happy Mothers Day!',True,'purple')
    screen.fill('light green')
    screen.blit(image3,(0,0))
#blit is a function to display anything on the screen

    screen.blit(text3,(150,300))
    pygame.display.update()
#this is the third image and the third text,font size,type and message to be displayed on the screen

    time.sleep(4)
#this is for how many seconds to wait for when the picture is changing in between the animation
pygame.quit()