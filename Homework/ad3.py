import tkinter as tk
import random

window = tk.Tk()
window.geometry("350x280") #調整遊戲視窗的大小
window.title("Guess number game")
window.configure(bg = "#FFE3CA") #調整遊戲視窗的背景顏色
guessNumber = ""
randomNumber = ""
plusScore = 0
score = 0
strRandomNumber = ""
strGuessNumber = ""
guessTime = 1

def click():
    global guessNumber
    global randomNumber
    global plusScore
    global score
    global strRandomNumber
    global strGuessNumber
    global guessTime
    
    try:
        guessNumber = EnterNumberEntry.get()
        if (00 <= int(guessNumber) <= 99):
            randomNumber = str(random.randrange(0,100))
            if(0<= int(randomNumber) <=9): #準確化亂數數字的格式
                randomNumber="0"+randomNumber
            if(len(guessNumber)==1): #準確化猜測數字的格式
                guessNumber="0"+guessNumber
            if(len(guessNumber)>2 and guessNumber[0]=="0"):
                guessNumber = guessNumber[len(guessNumber)-2] + guessNumber[len(guessNumber)-1]
            guessTime+=1 #確定輸入合格且準確畫格式之後,算是一輪猜測
            RoadLabel.config(text = "ROAD " + str(guessTime))
            if(randomNumber == guessNumber):#完全正確10分
                plusScore=10
            else:
                if(randomNumber[1] == guessNumber[1]):#任1數字正確且位置正確5分
                    plusScore+=5 #得分
                if(randomNumber[0] == guessNumber[0]):
                    plusScore+=5
                if(randomNumber[0] == guessNumber[1]):#任1數字正確但位置錯誤2分
                    plusScore+=2
                if(randomNumber[1] == guessNumber[0]):
                    plusScore+=2
            score+=plusScore   #更新累加分數     
            YourAnswer.config(text = "Your guess: " + guessNumber, fg = "black")
            Result.config(text = "Result: "+ randomNumber)
            PlusScore.config(text = "+"+ str(plusScore), fg = "blue")
            Score.config(text = " "+ str(score) + " ")
            plusScore=0
        else:
            YourAnswer.config(text = "Entry not valid", fg = "red")
            Result.config(text = "")
    except:
        YourAnswer.config(text = "Entry not valid", fg = "red")
        Result.config(text = "")
    EnterNumberEntry.delete(0,tk.END)

RoadLabel = tk.Label(window, text="ROAD " + str(guessTime),font=("Arial Bold", 20),bg = "#FFE3CA", height = 2)
TitleLabel = tk.Label(window, text = "Enter a number from 00 to 99",bg = "#FFE3CA")
EnterNumberEntry = tk.Entry(window)
Check = tk.Button(window, text = "Check",bg = "orange", command = click)
YourAnswer = tk.Label(window,bg = "#FFE3CA")
Result = tk.Label(window,bg = "#FFE3CA")
PlusScore = tk.Label(window,bg = "#FFE3CA")
Score = tk.Label(window, text = " 0 ", bg = "black", fg="white", font=("Arial Bold", 20))

RoadLabel.pack()
TitleLabel.pack()
EnterNumberEntry.pack()
Check.pack()
YourAnswer.pack()
Result.pack()
PlusScore.pack()
Score.pack()

window.mainloop()

