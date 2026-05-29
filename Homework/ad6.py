import pygame
import random
import time
from pygame.locals import *
pygame.init()

windowSize=[800,600]
screen=pygame.display.set_mode(windowSize)
pygame.display.set_caption("Football game")
clock = pygame.time.Clock() 

#射門座標
xCen=windowSize[0]//2
yCen=windowSize[1]//2
#玩家座標
playerX=xCen 
playerY=yCen
playerR=20
#球的座標
ballX=random.randrange(50,windowSize[0]-50)
ballY=random.randrange(200,windowSize[1]-50)
#黑色大射門
bigboxW=260
bigboxH=50
boxX=xCen-bigboxW/2
boxY=0
#3個紅黃藍小射門
smallboxW=70
smallboxH=20
redX=xCen-smallboxW/2
redY=15
yellowX=xCen-smallboxW/2+smallboxW+10
yellowY=15
blueX=xCen-smallboxW/2-smallboxW-10
blueY=15

score=0 #分數
plus=""
render=0
#count=1

white=pygame.color.Color("#ffffff")
green=pygame.color.Color("#2C7865")
playerCo=purple=pygame.color.Color("#E178C5")
scoreBoxCo=black=pygame.color.Color("#000000")
pink=pygame.color.Color("#FFD1E3")
red=pygame.color.Color("#D20062")
yellow=pygame.color.Color("#FFF455")
blue=pygame.color.Color("#5755FE")
orange=pygame.color.Color("#F2613F")

def randomColor(): 
    r=random.randrange(0,256)
    g=random.randrange(0,256)
    b=random.randrange(0,256)
    rgb="#%02x%02x%02x" % (r,g,b)
    return rgb
    
ballCo=pygame.color.Color(randomColor()) #隨機產生球的顏色

def randomOor(): #隨機產生球的座標
    global ballX
    global ballY
    ballX=random.randrange(250,windowSize[0]-250) 
    ballY=random.randrange(300,windowSize[1]-250)
    
def checkX(x): #玩家移出邊界外之處理
    if(x>windowSize[0]):
        x = 0
    elif(x<0):
        x = windowSize[0]
    return x

def checkY(y): #玩家移出邊界外之處理
    if(y>windowSize[1]):
        y = 0
    elif(y<0):
        y = windowSize[1]
    return y

def checkTouching(): #檢查玩家是否有踢到球,要是有會進行踢球的效應
    global playerX
    global playerY
    global ballX
    global ballY
    
    disX=playerX-ballX
    disY=playerY-ballY
    
    if(-1.5*playerR <=disX <= 1.5*playerR and -1.5*playerR <= disY <= 1.5*playerR):
        if ballX == 50:  #防止球卡在螢幕邊框的情況
            disX -= 15
        elif ballX == windowSize[0]-50:
            disX += 15
        if ballY == 50:
            disY -= 15
        elif ballY == windowSize[1]-50:
            disY += 15
        
        ballX -= disX * 3 #球被踢走的效應
        ballY -= disY * 3
        pygame.draw.line(screen, black, (playerX,playerY),(ballX,ballY),width=10)
    
font1 = pygame.font.SysFont('consolas',30) #font of game time
font2 = pygame.font.SysFont('consolas',20) #font of score

start=time.time() #紀錄遊戲開始的時間點
renderPlus=0
Time=120 #遊戲時間限制
done=False

while done==False:
    screen.fill(white)
    pygame.draw.rect(screen,green,(0,0,windowSize[0],windowSize[1]),width=50)
    pygame.draw.line(screen,green,(0,yCen),(windowSize[0],yCen),width=10)
    pygame.draw.circle(screen,green,(xCen,yCen),100,width=10)
    
    gametime=time.time()-start 
    textT=font2.render("Time",True,white)
    screen.blit(textT,(750,25))
    text=font1.render(str(gametime),True,white)
    screen.blit(text,(707,560)) #印出現在已玩多久時間
    if(gametime >=Time): #當下的時間量要是到達時間限制-->遊戲結束
        done=True
        
    pygame.draw.line(screen,pink,(775,50),(775,50+500),width=20) #顯示時間桿
    pygame.draw.line(screen,red,(775,50),(775,50+500/Time*gametime),width=10)
    
    pygame.draw.rect(screen,scoreBoxCo,[boxX,boxY,bigboxW,bigboxH]) #畫黑色大射門
    pygame.draw.rect(screen,red,[redX,redY,smallboxW,smallboxH]) #畫紅色小射門
    pygame.draw.rect(screen,yellow,[yellowX,yellowY,smallboxW,smallboxH]) #畫黃色小射門
    pygame.draw.rect(screen,blue,[blueX,blueY,smallboxW,smallboxH]) #畫藍色小射門
    
    keys = pygame.key.get_pressed()
    
    if keys [pygame.K_w]: 
        playerY-=1
        checkTouching()
    if keys [pygame.K_a]:
        playerX-=1
        checkTouching()
 
    if keys [pygame.K_s]:
        playerY+=1
        checkTouching()
 
    if keys [pygame.K_d]:
        playerX+=1
        checkTouching()

    if ballX<=50 or ballX>=windowSize[0]-50 or ballY<=50 or ballY>=windowSize[1]-50:
        #處理踢球到邊界之外的情況: -->直接給新球
        if boxX <= ballX <= boxX + bigboxW and ballY <= boxY + bigboxH:
            pass   #要是那個邊界屬於射門的部分就skip因為下面有處理了
        else:
            renderPlus=time.time()
            plus="Shot outside box:-1" #顯示球已被踢出邊界去
            score-=1
            ballCo=pygame.color.Color(randomColor()) #給新球
            randomOor()
            
    playerX=checkX(playerX) #檢查灣檢查灣家是否跑到邊界的處理
    playerY=checkY(playerY)
    
    text2=font2.render("Score",True,white)
    screen.blit(text2,(10,15))
    if(time.time()-renderPlus>=0.5): #進射門之後0,5秒內，顯示當時得到的分數
        plus=""
    for i in range(score): #畫分數:1顆球等於1分, 從上往下排
        scoreY=60+i*25
        pygame.draw.circle(screen,orange,(25,scoreY),10)
    
    pygame.draw.circle(screen,playerCo,[playerX,playerY],playerR,width=10) #玩家只畫外線->易於分辨哪個是玩家
    pygame.draw.circle(screen,ballCo,[ballX,ballY],playerR)
    text2=font2.render(plus,True,red) #顯示當時得到的分數
    screen.blit(text2,(playerX,playerY+20))  
    
    if boxX <= ballX <= boxX + bigboxW and ballY <= boxY + bigboxH: #進射門超過半顆球
        score += 1 #就算分數
        renderPlus=time.time()
        if yellowX <= ballX <= yellowX + smallboxW and ballY <= yellowY + smallboxH or blueX <= ballX <= blueX + smallboxW and ballY <= blueY + smallboxH:
            score += 1 # 球的中心點在黃色跟藍色小射門會得到2倍分數 
            plus="+2"
        else:
            plus="+1"
        ballCo=pygame.color.Color(randomColor()) #給新球
        randomOor()
        
    pygame.display.flip()
    #pygame.image.save(screen,"game"+str(count)+".jpg")
    #count+=1
      
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done=True
    clock.tick(72)
    
print("Total score: " + str(score))
pygame.quit()