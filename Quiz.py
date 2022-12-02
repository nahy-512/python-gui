BGCOLOR = "#21325E"
CORRECT_COLOR = "green"
WRONG_COLOR = "red"
BTN_COLOR = "#F0F0F0"

import csv
from tkinter import *
import random
import tkinter as tk
import GUI

questions = ["Q1) 여성 폭력 긴급 전화 번호는?",
             "Q2) 개인이 해야 할 일로 옳지 않은 것은?",
             "Q3) 2021년에 범죄가 가장 많이 일어난 지역은?",
             "Q4) 사회에서는 데이트 폭력 사건에 대비하기 위해 신고 시스템에 'ooo oo oo'을 신설하였는데 이는 무엇인가?"]

answers = [['1337','1366','1398','1388', '1366'],
           ['우편함에 각종 고지서 쌓아두지 않기','귀가 시 되도록 콜택시 이용하기','불분명한 이메일이나 첨부파일 그냥 열기','택시를 탈 때 휴대폰 와이파이와 위치켜기', '불분명한 이메일이나 첨부파일 그냥 열기'],
           ['서울','인천','대구','부산', '서울'],
           ['데이트 폭력 예방','데이트 폭력 코드','데이트 폭력 개선','데이트 폭력 방지', '데이트 폭력 코드']]
    
answer = 0    
index = -1
    
def next_question():
    global answer, index 
    
    index = index + 1
    
    if (index == 4):
        print('마지막 퀴즈 페이지')
        class main(tk.Frame):
            def __init__(self, master):
                tk.Button(self, text="Go back to main page", command=lambda: master.switch_frame(GUI.StartPage)).pack()
    
    for i in range(4):
        buttons[i].config(bg=BTN_COLOR)
    
    multi_choice = questions[index]
    correct_index=0
    for i in range(4):
        if(answers[index][i] == answers[index][4]):
            correct_index == i
            
    answer = answers[i]
    cur_question = questions[index]
    
    
    question_label.config(text=cur_question)
    
    for i in range(4):  
        buttons[i].config(text=answers[index][i])
        
    
    
#정답 체크
def check_answer(idx):
    idx = int(idx)
    if(answers[index][idx] == answers[index][4]):
        buttons[idx].config(bg=CORRECT_COLOR)
        #맞추면 자동으로 다음으로 넘어가기 (1000 = 1초)
        window.after(1000, next_question)
        
    else:
        buttons[idx].config(bg=WRONG_COLOR)
        
        
        
        
    
window = Tk()
window.title("퀴즈")
window.config(padx=30, pady =10, bg=BGCOLOR)

question_label = Label(window, width=20, height=2, text="test", 
                       font=("나눔바른펜", 25, "bold"), bg=BGCOLOR, fg="white")

question_label.pack(pady = 20)

buttons = []
for i in range(4):
    btn = Button(window, text=f"{i}번", width=35, height=2,
                 font=("나눔바른펜", 15, "bold"), bg=BTN_COLOR, command=lambda idx=i: check_answer(idx))
    btn.pack(pady = 10)
    buttons.append(btn)

# next_btn = Button(window, text="다음 문제", width=15, height=2,
#                   command=next_question,
#                   font=("나눔바른펜", 15, "bold"), bg="yellow")

# next_btn.pack(pady = 30)


next_question()

window.mainloop()