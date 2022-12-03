BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = "#3E497A"
BTN_COLOR = "#F0F0F0"

import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.geometry('570x700')

questions = ["Q1) 여성 폭력 긴급 전화 번호는?",
             "Q2) 개인이 해야 할 일로 옳지 않은 것은?",
             "Q3) 2021년에 범죄가 가장 많이 일어난 지역은?",
             "Q4) 사회에서는 데이트 폭력 사건에 대비하기 위해 신고 시스템에 'ooo oo oo'을 신설하였는데 이는 무엇인가?"]
options = [['1337','1366','1398','1388', '1366'],
           ['우편함에 각종 고지서 쌓아두지 않기','귀가 시 되도록 콜택시 이용하기','불분명한 이메일이나 첨부파일 그냥 열기','택시를 탈 때 휴대폰 와이파이와 위치켜기', '불분명한 이메일이나 첨부파일 그냥 열기'],
           ['서울','인천','대구','부산', '서울'],
           ['데이트 폭력 예방','데이트 폭력 코드','데이트 폭력 개선','데이트 폭력 방지', '데이트 폭력 코드']]


frame = tk.Frame(root, padx=10, pady=10,bg=BGCOLOR)
question_label = tk.Label(frame,height=5, width=28,bg=BGCOLOR,fg='white', 
                          font=('나눔바른펜', 25, "bold"),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Button(frame, bg=BTN_COLOR,width=45, height=2, font=('나눔바른펜', 15, "bold"),
                         command = lambda : checkAnswer(option1))
option2 = tk.Button(frame, bg=BTN_COLOR,width=45, height=2, font=('나눔바른펜', 15, "bold"), 
                         command = lambda : checkAnswer(option2))
option3 = tk.Button(frame, bg=BTN_COLOR,width=45, height=2, font=('나눔바른펜', 15, "bold"), 
                         command = lambda : checkAnswer(option3))
option4 = tk.Button(frame, bg=BTN_COLOR,width=45, height=2, font=('나눔바른펜', 15, "bold"),
                         command = lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',bg='Orange', width=15, height=2, font=('나눔바른펜', 15, "bold"), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=5, column=0)


index = 0
correct = 0

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    print("checkAnswer", index)
    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct +=1
        

    index +=1
    disableButtons('disable')


# create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
           question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'





    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'


displayNextQuestion()

root.mainloop()