BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = "#3E497A"
BTN_COLOR = "#F0F0F0"

import csv
from tkinter import *
import random

with open("quiz1.csv", "r", encoding="UTF-8-sig") as file:
    questions = list(csv.reader(file))
    
answer = 0    
    
def next_question():
    global answer
    
    for i in range(4):
        buttons[i].config(bg=BTN_COLOR)
    
    multi_choice = random.sample(questions, 4)
    answer = random.randint(0,3)
    cur_question = multi_choice[answer][0] 
    
    question_label.config(text=cur_question)
    
    for i in range(4):  
        buttons[i].config(text=multi_choice[i][2])
    
    
#정답 체크
def check_answer(idx):
    idx = int(idx)
    if(answer == idx):
        buttons[idx].config(bg=CORRECT_COLOR)
        #맞추면 자동으로 다음으로 넘어가기 (1000 = 1초)
        window.after(1000, next_question)
        
    else:
        buttons[idx].config(bg=WRONG_COLOR)
        buttons[idx]
        
    
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
    btn.pack()
    buttons.append(btn)

next_btn = Button(window, text="다음 문제", width=15, height=2,
                  command=next_question,
                  font=("나눔바른펜", 15, "bold"), bg=CORRECT_COLOR)

next_btn.pack(pady = 30)

next_question()

window.mainloop()