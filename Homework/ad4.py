import tkinter as tk  
import random
import time

window=tk.Tk()
window.title("Adjusting color game")
clickRed=0
clickGreen=0
clickBlue=0
color=""
starttime=0

def randomColor(): #亂數產生rgb,並顯示顏色與rgb值
    global color
    global clickRed
    global clickGreen
    global clickBlue
    #reset所有
    scoreLabel.config(text="Time:")
    clickRed=0
    clickGreen=0
    clickBlue=0
    redScale.set(clickRed)
    greenScale.set(clickGreen)
    blueScale.set(clickBlue)
    
    r=random.randrange(0,256)
    g=random.randrange(0,256)
    b=random.randrange(0,256)
    color = "#%02x%02x%02x" % (r,g,b)
    canvas.config(bg=color)
    Rlabel.config(text=r)
    Glabel.config(text=g)
    Blabel.config(text=b)

def up(color,value):
    global clickRed
    global clickGreen
    global clickBlue
    if(color=="red"):
        if(clickRed+value>255):
            clickRed=255
        elif(clickRed+value < 0):
            clickRed=0
        else:
            clickRed+=value
    if(color=="blue"):
        if(clickBlue+value>255):
            clickBlue=255
        elif(clickBlue+value < 0):
            clickBlue=0
        else:
            clickBlue+=value
    if(color=="green"):
        if(clickGreen+value>255):
            clickGreen=255
        elif(clickGreen+value < 0):
            clickGreen=0
        else:
            clickGreen+=value
    createColor()
    
def redDe1():
    up("red",-1)   
def greenDe1():
    up("green",-1) 
def blueDe1():
    up("blue",-1) 
def redIn1():
    up("red",1) 
def greenIn1():
    up("green",1) 
def blueIn1():
    up("blue",1) 

def redDe10():
    up("red",-10)
def greenDe10():
    up("green",-10)
def blueDe10():
    up("blue",-10)

def redIn10():
    up("red",10)
def greenIn10():
    up("green",10)
def blueIn10():
    up("blue",10)

#以當下的rgb值顯示顏色
def createColor():
    global clickRed
    global clickGreen
    global clickBlue
    global starttime
    global color
    #從按下任何一個按鈕開始計時間
    if(clickRed==0 and clickGreen==0 and clickBlue!=0
    or clickGreen==0 and clickBlue==0 and clickRed!=0
    or clickRed==0 and clickBlue==0 and clickGreen!=0):
        starttime=time.time()
    #顯示顏色
    resultColor="#%02x%02x%02x" % (clickRed,clickGreen,clickBlue)
    resultCanvas.config(bg=resultColor)
    #如果調出來的顏色跟亂數顏色一樣,顯示總花時間
    if(resultColor == color):
        score = time.time() - starttime
        scoreLabel.config(text="Time:"+str(score))
    redScale.set(clickRed)
    greenScale.set(clickGreen)
    blueScale.set(clickBlue)
    
button = tk.Button(window,text="Random",bg="black",fg="white",command=randomColor)
canvas=tk.Canvas(window, width=150,height=150) #亂數rgb的顏色

#rgb的亂數值
Rlabel=tk.Label(window,fg="#FF204E",font=("Arial",20))
Glabel=tk.Label(window,fg="#007F73",font=("Arial",20))
Blabel=tk.Label(window,fg="#1D24CA",font=("Arial",20))

#rgb的滑桿
redScale = tk.Scale(window,from_=0, to=255)
greenScale = tk.Scale(window,from_=0, to=255)
blueScale = tk.Scale(window,from_=0, to=255)

#-1按鈕
redDe1Button=tk.Button(window,text="-1",command=redDe1,width=6,height=3,bg="#FF407D")
greenDe1Button=tk.Button(window,text="-1",command=greenDe1,width=6,height=3,bg="#15F5BA")
blueDe1Button=tk.Button(window,text="-1",command=blueDe1,width=6,height=3,bg="#9195F6")

#+1按鈕
redIn1Button=tk.Button(window,text="+1",command=redIn1,width=6,height=3,bg="#FF407D")
greenIn1Button=tk.Button(window,text="+1",command=greenIn1,width=6,height=3,bg="#15F5BA")
blueIn1Button=tk.Button(window,text="+1",command=blueIn1,width=6,height=3,bg="#9195F6")

#-10按鈕
redDe10Button=tk.Button(window,text="-10",command=redDe10,width=6,height=3,bg="#FF407D")
greenDe10Button=tk.Button(window,text="-10",command=greenDe10,width=6,height=3,bg="#15F5BA")
blueDe10Button=tk.Button(window,text="-10",command=blueDe10,width=6,height=3,bg="#9195F6")

#+10按鈕
redIn10Button=tk.Button(window,text="+10",command=redIn10,width=6,height=3,bg="#FF407D")
greenIn10Button=tk.Button(window,text="+10",command=greenIn10,width=6,height=3,bg="#15F5BA")
blueIn10Button=tk.Button(window,text="+10",command=blueIn10,width=6,height=3,bg="#9195F6")

resultCanvas=tk.Canvas(window,width=150,height=150) #調出來的顏色
scoreLabel=tk.Label(window,font=("Arial",20),text="Time:") 

button.grid(row=1,column=1,columnspan=6)
canvas.grid(row=2,column=1,columnspan=6)
Rlabel.grid(row=3,column=1,columnspan=2)
Glabel.grid(row=3,column=3,columnspan=2)
Blabel.grid(row=3,column=5,columnspan=2)

redScale.grid(row=4,column=1,columnspan=2)
greenScale.grid(row=4,column=3,columnspan=2)
blueScale.grid(row=4,column=5,columnspan=2)

redDe1Button.grid(row=5,column=1)
greenDe1Button.grid(row=5,column=3)
blueDe1Button.grid(row=5,column=5)

redIn1Button.grid(row=5,column=2)
greenIn1Button.grid(row=5,column=4)
blueIn1Button.grid(row=5,column=6)

redDe10Button.grid(row=6,column=1)
greenDe10Button.grid(row=6,column=3)
blueDe10Button.grid(row=6,column=5)

redIn10Button.grid(row=6,column=2)
greenIn10Button.grid(row=6,column=4)
blueIn10Button.grid(row=6,column=6)

resultCanvas.grid(row=7,column=1,columnspan=6)
scoreLabel.grid(row=8,column=1,columnspan=6)

window.mainloop()