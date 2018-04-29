import pygame
import time
import random
from pygame import draw
pygame.init()

width=600
height=600


gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption('car race')
clock=pygame.time.Clock()
image = pygame.image.load('car1.png')
crashed_car= pygame.image.load('car5.png')
opp_car = pygame.image.load('opp.png')
black=(0, 0, 0)
white=(255, 255, 255)
red=(255, 0, 0)
grey=(128,128,128)
green=(50,205,50)


def car(x,y):
    gameDisplay.blit(image,(x,y))
def oppdisplay(x,y):

    gameDisplay.blit(opp_car,(x,y))
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()
def score1(score,x,y):
    font = pygame.font.SysFont(None, 25)
    text = font.render("score:"+str(score), True, white)
    gameDisplay.blit(text,(x,y))
def message_display(text,score):
    LargeText= pygame.font.Font("freesansbold.ttf", 50)
    Textsurf, TextRect = text_objects(text,LargeText)
    TextRect.center=((width/2),(height/2))
    gameDisplay.blit(Textsurf, TextRect)
    score1(score,(width/2)-20,(height/2)+40)
    pygame.display.update()

    time.sleep(1)
    main1()
def crash(text, score):
    message_display("YOU CRASHED",score)

def crashedcar(x,y):
    gameDisplay.blit(crashed_car,(x,y))
def rec(xr,yr,lr,wr):
    pygame.draw.rect(gameDisplay, white, (xr, yr, wr, lr))
def movingob(lanx,lany,lanw,lanh, color):
    pygame.draw.rect(gameDisplay,color,(lanx, lany, lanw, lanh))
    pygame.draw.rect(gameDisplay,color,(lanx, lany+150, lanw, lanh))
    pygame.draw.rect(gameDisplay,color,(lanx,lany+300,lanw,lanh))
    pygame.draw.rect(gameDisplay,color,(lanx,lany+450,lanw,lanh))
    pygame.draw.rect(gameDisplay,color,(lanx, lany-150, lanw, lanh))
    pygame.draw.rect(gameDisplay,color,(lanx, lany-300, lanw, lanh))
    pygame.draw.rect(gameDisplay,color,(lanx, lany-450, lanw, lanh))

def background():
    gameDisplay.fill(grey)



def main1():

    x=width*0.4
    y=height*0.7
    xr=50
    yr=10
    wr=10
    lr=20

    crashed=False
    xcar = 0
    y_start = -50
    x_start =20
    lanx=180
    lany = 10
    lanw =10
    lanh = 40
    lanx1 = 380
    score=0



    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            print(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xcar=-70
                elif event.key == pygame.K_RIGHT:
                    xcar=70
                else:
                    xcar = 0

            if event.type == pygame.KEYUP:
                if event.type == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                    xcar = 0

            x+=xcar


        background()


        # def movingob(lanx,lany,lanw,lanh, color):
        # ten = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        # for i in ten:
        # first lane
        movingob(lanx,lany,lanw,lanh,white)




        # second lane
        movingob(lanx1,lany,lanw,lanh,white)


        if score <= 3:
            lany+=1
        elif 4<=score<=10:
            lany+=1.5
        elif 10<=score<=20:
            lany+=2
        elif 20<=score<=40:
            lany+=2.5
        elif 30<=score:
            lany+=3


        if lany>= height:
            lany=10

        oppdisplay(x_start,y_start)
        if score <= 3:
            y_start+=1
        elif 4<=score<=10:
            y_start+=1.5
        elif 10<=score<=20:
            y_start+=2
        elif 20<=score<=40:
            y_start+=2.5
        elif 30<=score:
            y_start+=3
        if y_start>=height:
            score+=1
            y_start=-50
            ran = random.randrange(1,4)
            if ran ==1:
                x_start = 20
            elif ran==2:
                x_start = 240
            else:
                x_start = 440

        # pygame.draw.rect(gameDisplay, white, (50,10,10,20))
        car(x,y)
        score1(score,0,0)
        pygame.display.update()
        #boundary
        if x>(width-90) or x<0:
            # background()

            crashedcar(x,y)
            pygame.display.update()

            crash("you crashed",score)
        #     crashing car
        if y < y_start+172:

            if x > x_start and x< x_start+97 or x+97>x_start and x+97<x_start+97 or x==x_start:

                # background()
                crashedcar(x,y)
                pygame.display.update()
                crash("you crashed", score)

main1()
pygame.quit()
quit()