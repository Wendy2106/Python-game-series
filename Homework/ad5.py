import math
import pygame
import random

pygame.init()

windowSize = [800, 600]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

Cr=50  #圓形半徑
xC = windowSize[0] // 2 #圓形的中心座標
yC = windowSize[1] // 2 - 180 
Cspeed=0.05  #影響到圓形晃動的範圍以及大小變化
countC = 0

Rwidth=Rheight=30
xR = windowSize[0] // 2 -0.5*Rwidth #讓矩形在螢幕中間座標 
yR = windowSize[1] // 2 + 150
Rdir="right" #矩形當下的方向
ROpdir="left" #矩形當下的相反方向

black = pygame.color.Color("#000000") #背景顏色
circleColour = pygame.color.Color('#EEE4B1') #圓形的原始顏色
rectColour = pygame.color.Color('#F7418F') #矩形的顏色

def changeDirection(x):
    if(xR >= windowSize[0]-2*Rwidth):  #要是矩形碰到右邊的邊框
        return -10  #向左移
    else:   #要是舉行碰到左邊的邊框
        return 10   #向右移

done = False
while not done:
    screen.fill(black)
    
    pygame.draw.circle(screen, circleColour, [xC, yC], Cr)
    pygame.draw.circle(screen, black, [xC, yC], Cr/2) 
    xC += (math.cos(countC)*10) /2
    yC += (math.sin(countC)*10) /2
    Cr+=math.sin(countC) #改變半徑,讓顏形大小有變化(遠小-近大)
    
    pygame.draw.rect(screen, rectColour, [xR, yR, Rwidth, Rheight])
    pygame.draw.rect(screen, rectColour, [xR-Rwidth/2, yR-Rheight/2, 2*Rwidth,2*Rheight],width=5)
    # 矩形的左右移動
    if(xR <= windowSize[0] and Rdir =="right"): #矩形完全在螢幕裡, 方向是向右移
        xR+=10 #繼續向右移
    elif(xR <= windowSize[0] and Rdir =="left"): #矩形完全在螢幕裡, 方向是向左移
        xR-=10 #繼續向左移  
    if(xR >= windowSize[0]-1.25*Rwidth or xR <= Rwidth/4):#矩形碰到螢幕的邊框
        #換方向
        oldDir=Rdir
        Rdir=ROpdir
        ROpdir=oldDir
        xR+=changeDirection(xR)
        
        #換圓形的顏色
        r=random.randrange(0,256)
        g=random.randrange(0,256)
        b=random.randrange(0,256)
        
        newCColor="#%02x%02x%02x" % (r,g,b)
        circleColour=newCColor;
    
    countC += Cspeed 
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    clock.tick(50)

pygame.quit()
