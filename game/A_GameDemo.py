import pygame
import time
pygame.init()

windowSize = [1077, 590]
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("你抓寶還是鬼抓你?")
clock = pygame.time.Clock()
Time=20 #遊戲時間(s)

white = pygame.color.Color("#ffffff")
yellow= pygame.color.Color("#FFBB70")
red= pygame.color.Color("#C40C0C")
green= pygame.color.Color("#697235")
orange = pygame.color.Color("#f0921c")

font1= pygame.font.SysFont('arial', 100, bold=True)
textL1=font1.render("1",True,white)
textL2=font1.render("2",True,white)
font2= pygame.font.SysFont('consolas', 20)
textP1=font2.render("1",True,white)
textP2=font2.render("2",True,white)
font3= pygame.font.SysFont('arial', 60, bold=True)
font4= pygame.font.SysFont('arial', 85, bold=True)

pygame.mixer.music.load('menuMusic.mp3') #等待等待模式的音樂
pygame.mixer.music.play(-1)

collect=pygame.mixer.Sound('collect.mp3')#收集金幣的音效
store=pygame.mixer.Sound('store.mp3')#存放金幣的音效
ohoh=pygame.mixer.Sound('ohoh.mp3')#被鬼抓的音效
gameOver = pygame.mixer.Sound('gameOver.mp3')#輸的音效
playerWin = pygame.mixer.Sound('playerWin.mp3')#贏得勝利的音效
wee = pygame.mixer.Sound('wee.mp3')#最後2個玩家沒死，但有一個的金幣比較多的音效

menu = pygame.image.load('menu.png')
bg = pygame.image.load('bg.png')
sticker = pygame.image.load('sticker.png')
resultEvilEat = pygame.image.load('resultEvilEat.png')
resultCoinMany = pygame.image.load('resultCoinMany.png')
resultCoinEqual = pygame.image.load('resultCoinEqual.png')

#玩家一的圖檔
down11 = pygame.image.load('down1.png')
down12 = pygame.image.load('down2.png')
down13 = pygame.image.load('down3.png')
up11 = pygame.image.load('up1.png')
up12 = pygame.image.load('up2.png')
up13 = pygame.image.load('up3.png')
left11 = pygame.image.load('side1.png')
left12 = pygame.image.load('side2.png')
left13 = pygame.image.load('side3.png')
right11 = pygame.transform.flip(left11, True, False)
right12 = pygame.transform.flip(left12, True, False)
right13 = pygame.transform.flip(left13, True, False)

#玩家二的圖檔
down21 = pygame.image.load('player2down1.png')
down22 = pygame.image.load('player2down2.png')
down23 = pygame.image.load('player2down3.png')
up21 = pygame.image.load('player2up1.png')
up22 = pygame.image.load('player2up2.png')
up23 = pygame.image.load('player2up3.png')
left21 = pygame.image.load('player2side1.png')
left22 = pygame.image.load('player2side2.png')
left23 = pygame.image.load('player2side3.png')
right21 = pygame.transform.flip(left21, True, False)
right22 = pygame.transform.flip(left22, True, False)
right23 = pygame.transform.flip(left23, True, False)

#小鬼與金幣的圖檔
ghost1 = pygame.image.load('ghost1.png')
ghost2 =pygame.transform.flip(ghost1, True, False)
coin1 = pygame.image.load('coin1.png')
coin2 = pygame.image.load('coin2.png')
coin3 = pygame.image.load('coin3.png')
coin4 = pygame.image.load('coin4.png')
coin5 = pygame.image.load('coin5.png')
coin6 = pygame.image.load('coin6.png')
coin7 = pygame.image.load('coin7.png')
coin8 = pygame.image.load('coin8.png')
coin9 = pygame.image.load('coin9.png')

wsx = windowSize[0] #縮寫因為偷懶打而已:>
wsy = windowSize[1]

ghostSpeed=1 #小鬼移動速度
#鬼之地的地標
ghostLeftLandmarkX = wsx/2-200 
ghostRightLandmarkX = wsx/2+200
#小鬼座標
ghX= wsx/2-50
ghY= wsy/2-50
speed=2 #人物移動速度
#玩家一座標
x1 = 260-64 
y1 = 577/2-64
#玩家二座標
x2 = wsx-260
y2 = 577/2-64

#避免人物走過螢幕範圍
def checkOffScreenX(x):
    global windowSize
    if x > windowSize[0]-64:
        x = windowSize[0]-64
    elif x < 0:
        x =  0
    return x

def checkOffScreenY(y):
    global windowSize
    if y >= windowSize[1]-120:
        y = windowSize[1]-120
    elif y < 0:
        y = 0
    return y

#製造人物移動，金幣轉圈圈的效果
countCoin=0
count=0
coinImages=[coin1,coin2,coin3,coin4,coin5,coin6,coin7,coin8,coin9]
downPlayer1=[down11,down12,down13]
upPlayer1=[up11,up12,up13]
leftPlayer1=[left11,left12,left13]
rightPlayer1=[right11,right12,right13]
downPlayer2=[down21,down22, down23]
upPlayer2=[up21,up22,up23]
leftPlayer2=[left21, left22,left23]
rightPlayer2=[right21,right22,right23]

#動畫
def animation(images,speedImage,object): 
    global countCoin,count
    index = int(countCoin) if object=="coin" else count//5
    if object=="coin":
        countCoin = (countCoin + speedImage) % len(images)
    else:
        count = (count + speedImage) % 15
    return images[index]

lockCollection=[False]*3 #鎖定玩家i的收集功能，一次只能偷取1顆金幣
storeCoinPosition1=[] #玩家1可存放金幣的座標
storeX1=80-32
storeY=coinY=150
storeCoinPosition2=[] #玩家2可存放金幣的座標
storeX2=wsx-80
coins=[] #金幣i當下的座標
storing=[False]*6 #狀態:金幣i正在去存放的過程中
owner=[] #金幣i的主人
haveCoin=[True]*6 + [False]*6 #狀態:位置i有金幣
totalCoin1=totalCoin2=3 #兩個玩家的總擁有的金幣
posInhaveCoin=[] #金幣i在haveCoin相應的位置

#產生各陣列的元素
for i in range(6):
    posInhaveCoin.append(i)
    storeCoinPosition1.append((storeX1,storeY))
    storeCoinPosition2.append((storeX2,storeY))
    storeY+=50
    
for i in range(3):
    coins.append(((storeX1,coinY)))
    owner.append(1)
    coins.append(((storeX2,coinY)))
    owner.append(2)
    coinY+=50

#在玩家的金幣存放區，從上往下，找沒有存放金幣的位置 (為了好看及整齊)
def notHaveCoinPos(player):
    k=0
    if player==2: 
        k+=1   
    for i in range(k,12,2):
        if not haveCoin[i]:
            return i

#收集金幣
def collectCoin(i,player,x,y):
    global owner,lockCollection,storing,\
        totalCoin1,totalCoin2,haveCoin,posInhaveCoin
        
    if not storing[i] and owner[i]!=player\
        and x<coins[i][0]<x+64 and y<coins[i][1]<y+64:
        collect.play()
        owner[i]=player #金幣換主人
        lockCollection[player]=True #鎖定玩家收集功能
        storing[i]=True #標記正在運送去存放的過程中，避免另外那個玩家中途搶金幣
        if player==1: #計算2玩家總金幣
            totalCoin1 += 1 
            totalCoin2-=1
        else:
            totalCoin2 += 1
            totalCoin1-=1
        haveCoin[posInhaveCoin[i]]=False #標記此標記此位置已經沒有金幣了
           
#存放金幣i       
def storeCoin(i,player,x,y):
    global ghostLeftLandmarkX,ghostRightLandmarkX,coins,\
        storeCoinPosition1,storeCoinPosition2,\
        lockCollection,storing,haveCoin,posInhaveCoin
        
    if (player == 1 and x < ghostLeftLandmarkX - 80) \
        or (player == 2 and x > ghostRightLandmarkX + 80):
            notHaveCoinXY = notHaveCoinPos(player) #找沒有金幣的位置
            coins[i] = storeCoinPosition1[notHaveCoinXY // 2] \
                if player == 1 else storeCoinPosition2[notHaveCoinXY // 2]\
                    #在沒有金幣的位置，存放此金幣
            store.play()
            posInhaveCoin[i] = notHaveCoinXY #更新此金幣的位置
            haveCoin[notHaveCoinXY] = True #標記此位置有金幣
            storing[i] = False  # 標記已完成存放金幣
            lockCollection[player] = False #開放玩家的收集功能
            
#檢查哪一個玩家進入魔鬼之地
def inGhostArea():
    global x1,y1,x2,y2,ghostLeftLandmarkX,ghostRightLandmarkX
    result=0
    if ghostLeftLandmarkX<= x1 and x1+64 <= ghostRightLandmarkX:
        result+=1   
    if ghostLeftLandmarkX<= x2 and x2+64 <= ghostRightLandmarkX:
        result+=2
    return result #玩家1進入=>1,玩家2進入=>2,兩個玩家都進入=>3

#要是2個玩家都進入,確定在魔鬼之地離小鬼最近的玩家(x,y)
def near(object): 
    global x1,x2,y1,y2,ghX,ghY
    #計算小鬼與2個玩家之間的距離
    distance1 = ((x1-ghX)**2+(y1-ghY)**2)**0.5 
    distance2 = ((x2-ghX)**2+(y2-ghY)**2)**0.5
    if distance1 < distance2: #比較距離 - >return最近的
        return x1 if object=="x" else y1
    else:
        return x2 if object=="x" else y2

#計算魔鬼往玩家移動的座標
def followX(x):
    global ghX,ghY,ghostSpeed
    if ghX-x<0:
        return ghostSpeed
    elif -5<ghX-x<5:
        return 0
    elif ghX-x>0:
        return -ghostSpeed
    
def followY(y):
    global ghX,ghY,ghostSpeed
    if ghY-y<0:
        return ghostSpeed
    elif ghY-y==0:
        return 0
    elif ghY-y>0:
        return -ghostSpeed   

#小鬼的移動
ghDirection = "left" #小鬼在沒有外來者進入鬼之地的移動的方向
ghost=ghost1 #小鬼當下的圖檔
def ghostMove():
    global ghX,ghY,ghDirection,ghost,ghost1,ghost2,\
        x1,y1,x2,y2,ghostSpeed
        
    if inGhostArea()!=0: #有玩家在鬼之地裡的情況
        flX=followX(x1) if inGhostArea()==1 \
            else (followX(x2) if inGhostArea()==2 \
                else followX(near("x"))) 
        flY=followY(y1) if inGhostArea()==1 \
            else(followY(y2) if inGhostArea()==2 \
                else followY(near("y")))
        #如果目標在鬼當下的移動方向->回頭再追
        if flX==-ghostSpeed and ghost==ghost2:
            ghost=ghost1 
        elif flX==ghostSpeed and ghost==ghost1:
            ghost=ghost2
        #追捕
        ghX+=flX 
        ghY+=flY
    elif ghDirection == "left" and ghX>ghostLeftLandmarkX:
        ghX-=ghostSpeed
        ghost=ghost1
    elif ghDirection == "right" and ghX+100<ghostRightLandmarkX:
        ghX+=ghostSpeed
        ghost=ghost2
    elif ghDirection == "left" and ghX<=ghostLeftLandmarkX:#到左邊邊界->回頭
        ghDirection="right"
        ghX+=ghostSpeed
    elif ghDirection == "right" and ghX+100>=ghostRightLandmarkX:#到右邊邊界->回頭
        ghDirection="left"
        ghX-=ghostSpeed
        
#確認玩家是否死亡/被鬼抓到        
def dier():
    global ghX,ghY,x1,y1,x2,y2
    if ghX-20<=x1<=ghX+60 and ghY-30<=y1<=ghY+80:
        return 1 #玩家1死亡
    elif ghX-20<=x2<=ghX+60 and ghY-30<=y2<=ghY+80:
        return 2 #玩家2死亡
    else:
        return 0 #沒有玩家死亡

gameResult=["","PLAYER 1 WINS","PLAYER 2 WINS","THIS MATCH WAS A TIE"]                          
gameResultFullText=""

def printResult(): #輸出比分+遊戲結果
    global totalCoin1,totalCoin2, gameResultFullText
    print("Player 1 | Player 2:\n")
    gameResultFullText+="   "+str(totalCoin1)+"           "+str(totalCoin2)
    print(gameResultFullText)
    if totalCoin1==totalCoin2:
        print(gameResult[3])
    else:
        wee.play() #音效有玩家贏
        pygame.time.delay(1000)
        if totalCoin1>totalCoin2:
            print(gameResult[1])
        elif totalCoin1<totalCoin2:
            print(gameResult[2])


outMenu=False 
while(not outMenu):
    screen.blit(menu, (0,0))
    # pygame.draw.rect(screen,white,(645,390,230,100),width=1)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            outMenu= True 
        if event.type == pygame.MOUSEBUTTONDOWN : 
            (a,b) = pygame.mouse.get_pos()
            if 645<=a<=875 and 390<=b<=490:
                outMenu=True #跳脫等待模式 ->進入遊戲
                startTime=time.time()
                pygame.mixer.music.stop() 
                pygame.mixer.music.load('creepy.mp3') #開遊戲音樂
                pygame.mixer.music.play(-1)
                done = False
                while not done:
                    screen.blit(bg, (0, 0))
    
                    #時間顯時間顯示                                          
                    gameTime=time.time()-startTime
                    pygame.draw.line(screen,yellow,(wsx/2-250,wsy-20),(wsx/2+250,wsy-20),width=20) #畫時間桿
                    pygame.draw.line(screen,red,(wsx/2-250,wsy-20),(wsx/2-250+500/Time*gameTime,wsy-20),width=10)
                    screen.blit(sticker,(wsx/2-250+500/Time*gameTime-20,wsy-33))  
                            
                    screen.blit(ghost, (ghX, ghY))
                    ghostMove()
    
                    for i in range(6):
                        coin=animation(coinImages,0.2,"coin")
                        if not lockCollection[1]:
                            collectCoin(i,1,x1,y1)
                        if not lockCollection[2]:
                            collectCoin(i,2,x2,y2)
        
                        if storing[i]==True :
                            if owner[i] in [1, 2]:
                                x = x1 if owner[i] == 1 else x2
                                y = y1 if owner[i] == 1 else y2
                                coins[i] = (x + 16, y - 30)
                                storeCoin(i, owner[i], x, y)
                        screen.blit(coin,(coins[i][0],coins[i][1]))
        
                    keys = pygame.key.get_pressed()
   
                    if keys[pygame.K_s]:
                        imagePlayer1 = animation(downPlayer1,1,"player")
                        y1 += speed
                    elif keys[pygame.K_w]:
                        imagePlayer1 = animation(upPlayer1,1,"player")
                        y1 -= speed
                    elif keys[pygame.K_a]:
                        imagePlayer1 = animation(leftPlayer1,1,"player")
                        x1 -= speed
                    elif keys[pygame.K_d]:
                        imagePlayer1 = animation(rightPlayer1,1,"player")
                        x1 += speed
                    else:
                        imagePlayer1 = down12
                        
                    x1=checkOffScreenX(x1)
                    y1=checkOffScreenY(y1)
                    screen.blit(imagePlayer1, (x1,y1))  
                    screen.blit(textP1,(x1+25,y1+60))  
    
                    if keys[pygame.K_DOWN]:
                        imagePlayer2 = animation(downPlayer2,1,"player")
                        y2 += speed
                    elif keys[pygame.K_UP]:
                        imagePlayer2 = animation(upPlayer2,1,"player")
                        y2 -= speed
                    elif keys[pygame.K_LEFT]:
                        imagePlayer2 = animation(leftPlayer2,1,"player")
                        x2 -= speed
                    elif keys[pygame.K_RIGHT]:
                        imagePlayer2 = animation(rightPlayer2,1,"player")
                        x2 += speed
                    else:
                        imagePlayer2 = down22

                    x2=checkOffScreenX(x2)
                    y2=checkOffScreenY(y2)
                    screen.blit(imagePlayer2, (x2,y2))
                    screen.blit(textP2,(x2+25,y2+60))
    
                    #其中1個玩家被鬼抓->剩下來的玩家贏->直接輸出遊戲結果(沒有比分)
                    if dier()!=0:
                        ohoh.play()
                        print("Player "+str(dier())+" died (╥﹏╥)")
                        print(gameResult[2]) if dier()==1 else print(gameResult[1])
                        pygame.mixer_music.pause()

                        #here can add a screen: background, the winner, and result
                        #顯示其中玩家被鬼抓的遊戲結果畫面
                        screen.blit(resultEvilEat, (0,0))
                        
                        #寫上被鬼抓的玩家
                        textDier=font3.render(str(dier()),True, green)
                        screen.blit(textDier,(575,200)) 
                        winner=3-dier() #剩下來是獲得勝利的玩家
                        textWinner=font1.render(str(winner),True, orange)
                        screen.blit(textWinner,(650,283))
                        pygame.display.flip()
                        
                        gameOver.play() 
                        pygame.time.delay(5000)
                        done=True
                    #時間結束，沒有哪一個玩家死，輸出遊戲的比分與結果
                    elif gameTime>=Time: 
                        printResult() #print on the terminal screen 
                        pygame.mixer_music.pause()
                        #若結果不平局
                        if totalCoin1!=totalCoin2:
                            screen.blit(resultCoinMany, (0,0)) #bg
                            textTotalCoin=font4.render(gameResultFullText,True, green)
                            screen.blit(textTotalCoin,(550,190)) #result
                            textWinner=font1.render("1" if totalCoin1>totalCoin2 else "2",True, orange)
                            screen.blit(textWinner,(650,280))
                        else:
                            screen.blit(resultCoinEqual, (0,0))
                            textTotalCoin=font4.render(gameResultFullText,True, green)
                            screen.blit(textTotalCoin,(550,190)) #result
                        pygame.display.flip()

                        playerWin.play()
                        pygame.time.delay(5000)
                        done=True
        
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                    pygame.display.flip()
                    clock.tick(64)
pygame.quit()
        