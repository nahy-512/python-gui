BGCOLOR = "#21325E"
CORRECT_COLOR = "green"
WRONG_COLOR = "red"
BTN_COLOR = "#F0F0F0"


import tkinter as tk
import csv
from tkinter import *
import random
import GUI
    
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

#메인 페이지
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # 메인페이지 인증 문구
        tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        # 범죄 시간대 확인 버튼
        tk.Button(self, text="범죄 시간대 확인", height = 3, width = 20,
                  command=lambda: master.switch_frame(crime_time_zone)).pack(pady=5)
        # 범죄 지역 확인 버튼
        tk.Button(self, text="범죄 지역 확인", height = 3, width = 20,
                  command=lambda: master.switch_frame(crime_area)).pack(pady=5)
        # 예방방법 버튼
        tk.Button(self, text="예방 방법", height = 3, width = 20,
                  command=lambda: master.switch_frame(prevention)).pack(pady=5)
        # 퀴즈 버튼
        tk.Button(self, text="퀴즈", height = 3, width = 20,
                  command=lambda: master.switch_frame(Quiz)).pack(pady=5) 
        
        # Btn1.grid(row=1, column=2)
        # Btn2.grid(row=3, column=2)
        # Btn3.grid(row=5, column=2)
        # Btn4.grid(row=7, column=2)

#범죄 시간 확인 버튼 눌렀을때 뜨는 페이지
class crime_time_zone(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

#범죄 지역 확인 버튼 눌렀을 때 뜨는 페이지
class crime_area(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

#예방 방법 버튼 눌렀을 때 뜨는 페이지
class prevention(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        
        
#퀴즈 버튼 눌렀을 때 뜨는 페이지
class Quiz(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("300x350")
    app.mainloop()