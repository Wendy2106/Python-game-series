import pygame
import random
import time

pygame.init()
windowSize = [800, 800]
ws = windowSize[0]
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Way back home")
clock = pygame.time.Clock()

downl = pygame.image.load('down1.png')
down2 = pygame.image.load('down2.png')
down3 = pygame.image.load('down3.png')
upl = pygame.image.load('up1.png')
up2 = pygame.image.load('up2.png')
up3 = pygame.image.load('up3.png')
leftl = pygame.image.load('side1.png')
left2 = pygame.image.load('side2.png')
left3 = pygame.image.load('side3.png')
rightl = pygame.transform.flip(leftl, True, False)
right2 = pygame.transform.flip(left2, True, False)
right3 = pygame.transform.flip(left3, True, False)
box = pygame.image.load('box.png')
heart=pygame.image.load('heart.png')
boom = pygame.image.load('boom.png')
bumm = pygame.image.load('bumm.png')
home = pygame.image.load('home.png')

white = pygame.color.Color("#ffffff")
brown = pygame.color.Color("#803D3B")
green = pygame.color.Color("#41B06E")
yellow= pygame.color.Color("#FFBB70")
red= pygame.color.Color("#C40C0C")

count = 0
x = ws/2-32
y = 0

xline = 0
yline = 100
road = [] #存所有機關的座標，共有18個
roadW=ws/3 #每個機關的寬度
roadH=50 #高度

life=3 #每一局玩家有3條命
boxImage=[] #存所有機關的箱子與箱子裡隱藏秘密物品的照片
roadColor =[] #機關顏色的陣列
opened=[] #箱子狀態的陣列
end=False #確認玩家是否回到家的變數
font = pygame.font.SysFont('consolas',20)
startGame=time.time()
renderTime=0
boomTime=0
fighting=""

pygame.mixer.music.load('gameMusic.mp3')
pygame.mixer.music.play(-1)
laugh = pygame.mixer.Sound('laugh.mp3')
ohoh = pygame.mixer.Sound('ohoh.mp3')
explosion = pygame.mixer.Sound('explosion.mp3')
gameOver = pygame.mixer.Sound('gameOver.mp3')
win = pygame.mixer.Sound('win.mp3')

def move(image1, image2 , image3):
    global count
    if count < 5:
        image = image1
    elif 5 <= count < 10:
        image = image2
    elif count >= 10:
        image = image3
   
    if count >= 15:
        count = 0
    else:
        count += 1
    return image

#存機關座標到陣列裡
for i in range (6):
        for u in range(3):
            road.append((xline,yline))
            xline+=ws/3
        xline=0
        yline+=100


for i in range(18):
    opened.append(False)
    boxImage.append(box)
    roadColor.append(brown)
 
#檢查人物是否踩到機關，如果有會改變機關的顏色
def check():
    global x
    global y
    global roadColor
    global yellow
    global road
    global roadH
    global roadW
    for i in range(18):
        if road[i][0]<= x+50 <= road[i][0]+roadW and road[i][1]<= y+50 <= road[i][1]+roadH:
            roadColor[i]=yellow
            break
 
#隨機決定箱子裡的物品
def randomMystery(one,two,three):
    mystery = random.randrange(1,4)
    if mystery == 1:
        return one
    elif mystery ==2:
        return two
    elif mystery ==3:
        return three
   
#檢查人物是否回到家
def checkEndGame():
    global x
    global y
    global end
    global ws
    if ws/3 <= x+50 <= ws/3+ws/3 and 750 <= y+50 <= 750+ws/3:
        win.play()
        pygame.time.delay(3000)
        end=True  

done = False
while not done:
    screen.fill(white)
   
    pygame.draw.rect(screen,green,(0,0,ws,ws/12)) #畫人物出始要站著的區域
    pygame.draw.rect(screen,green,(0,600,ws,ws/8*2)) #人物家周邊的區域
    pygame.draw.rect(screen,red,(ws/3,750,ws/3,ws/3)) #人物家的區域
   
    textL=font.render("Life:",True,white) #顯示當下玩家還有幾條命
    screen.blit(textL,(625,25))
    xlife=700
    for i in range(life):
        pygame.draw.circle(screen,red,(xlife,33),10)
        xlife+=25
       
    if time.time()-renderTime>1: #誇獎與提醒顯示
        fighting=""
    textF=font.render(fighting,True,white)
    screen.blit(textF,(25,25))
   
   
    #畫機關跟顯示箱子的狀態
    for i in range(18):
        pygame.draw.rect(screen,roadColor[i],(road[i][0],road[i][1],roadW,roadH))
        if opened[i] == False and roadColor[i]==yellow: #箱子未打開和玩家踩到該箱子的機關
            boxImage[i] = randomMystery(heart,boom,heart) #出現隨機物品:炸彈(1/3)與愛心(2/3)
            if boxImage[i]==boom: #要是出來的物品是炸彈
                ohoh.play()
                fighting="Oh no you stepped on the bomb" #通知
                boomTime=time.time() #計算該爆炸時間
            else:
                laugh.play()
                fighting="Yeah! So great. Let's continue"
            renderTime=time.time()
            opened[i]=True #標註此箱子已打開
           
        diff=0
        if boxImage[i]==boom and opened[i]==True and time.time()-boomTime>=0.5:#從打開盒子到此時到達0.5秒->顯示爆炸
            explosion.play()
            boxImage[i]=bumm
            life-=1 #人物死一命
        if boxImage[i]==bumm:
            diff=-40 #調整爆炸元素的位置(因為他比較大)
        screen.blit(boxImage[i],((road[i][0] + roadW/2)-30+diff, road[i][1]+45+diff))
           
    # 兩條白線
    pygame.draw.line(screen,white,(ws/3,100),(ws/3,650),width=5)
    pygame.draw.line(screen,white,(ws/3*2,100),(ws/3*2,650),width=5)
   
    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_s]:
        image = move(downl, down2, down3)
        y += 1
    elif keys[pygame.K_w]:
        image = move(upl, up2, up3)
        y -= 1
    elif keys[pygame.K_a]:
        image = move(leftl, left2, left3)
        x -= 1
    elif keys[pygame.K_d]:
        image = move(rightl, right2, right3)
        x += 1
    else:
        image = down2
        count = 0

    screen.blit(image, (x, y))
    screen.blit(home, (350,680))
    check()
    checkEndGame()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT or life<=0 or end==True:
            done = True #按叉叉，命剩下0或人物回到家->跳脫遊戲
            if life<=0:
                gameOver.play()
                pygame.time.delay(1000)
    pygame.display.flip()
    clock.tick(64)

pygame.quit()
if end==True and life > 0: #顯示這一局遊戲的結果
    print("WIN")
elif life <= 0:
    print("GAME OVER")