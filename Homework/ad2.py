import turtle 
t = turtle.Turtle()
t.speed(0)

sizeShape = 3 #可以改, 用於調整大小
#以大小比例計算出比的粗細度,半徑,與距離
penSize = 6*sizeShape 
t.pensize(penSize)
r = 29.5*sizeShape
distance = 10.7*sizeShape
#設定每一個環形下筆的座標
aBlack = 0
bBlack = 0
aRed = aBlack+2*r+distance
bRed = 0
aBlue = aBlack-(2*r+distance)
bBlue = 0
aGreen = (2*r+distance)/2
bGreen = -r
aYellow = -((2*r+distance)/2)
bYellow = -r

def moving(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#畫沒有重疊的部分
moving(aBlue,bBlue)
t.color("blue")
t.circle(r,45)
t.penup() #到有重疊的圓弧就拿起筆尖, 不畫重疊的部分
t.circle(r,45)
t.pendown() #過了重疊的圓弧,下筆繼續畫
t.circle(r,270)
#以此類推...
moving(aBlack , bBlack)
t.color("black")
t.circle(r,45)
t.penup()
t.circle(r,45)
t.pendown()
t.circle(r,225)
t.penup()
t.circle(r,45)
t.pendown()

moving(aRed , bRed)
t.color("red")
t.circle(r,315)
t.penup()
t.circle(r,45)
t.pendown()

moving(aYellow,bYellow)
t.color("yellow")
t.circle(r,135)
t.penup()
t.circle(r,45)
t.pendown()
t.circle(r,45)
t.penup()
t.circle(r,45)
t.pendown()
t.circle(r,90)

moving(aGreen,bGreen)
t.color("green")
t.circle(r,135)
t.penup() 
t.circle(r,45)
t.pendown()
t.circle(r,45)
t.penup()
t.circle(r,45)
t.pendown()
t.circle(r,90)

#畫重疊的部分

moving(aBlue,bBlue)
t.color("blue")
t.penup() #到沒有重疊的圓弧就拿起筆尖, 不畫
t.circle(r,45)
t.pendown() #直到重疊的圓弧,才下筆畫
t.circle(r,46) #因因為筆尖的形狀式圓形,所以這裡有調整多畫長一度讓第二次填補痕跡部會很明顯
t.penup()
t.circle(r,269)
t.pendown()
#以此類推...
moving(aBlack , bBlack)
t.color("black")
t.penup()
t.circle(r,45)
t.pendown()
t.circle(r,46) #因因為筆尖的形狀式圓形,所以這裡有調整多畫長一度讓第二次填補痕跡部會很明顯
t.penup()
t.circle(r,224)
t.pendown()
t.circle(r,45)

moving(aRed , bRed)
t.color("red")
t.penup()
t.circle(r,315)
t.pendown()
t.circle(r,45)

moving(aYellow,bYellow)
t.color("yellow")
t.penup()
t.circle(r,135)
t.pendown()
t.circle(r,45)
t.penup()
t.circle(r,45)
t.pendown()
t.circle(r,45)
t.penup()
t.circle(r,90)
t.pendown()

moving(aGreen,bGreen)
t.color("green")
t.penup()
t.circle(r,135)
t.pendown()
t.circle(r,45)
t.penup()
t.circle(r,45)
t.pendown()
t.circle(r,45)
t.penup()
t.circle(r,90)
t.pendown()

turtle.mainloop()
