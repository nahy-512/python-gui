BGCOLOR = "#21325E"
CORRECT_COLOR = "green"
WRONG_COLOR = "red"
BTN_COLOR = "#F0F0F0"


import tkinter as tk
import csv
from tkinter import *
import random
from PIL import Image, ImageTk
import gui_module



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

class secondApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(prevention)

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

#범죄 시간 확인 버튼 눌렀을때 뜨는 페이지
class crime_time_zone(tk.Frame):
    def __init__(self, master):
        app.geometry("300x350")
        tk.Frame.__init__(self, master)
        gui_module.frame_crime_time(self) # 범죄 시간 화면
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

#범죄 지역 확인 버튼 눌렀을 때 뜨는 페이지
class crime_area(tk.Frame):
    def __init__(self, master):
        app.geometry("300x350")
        tk.Frame.__init__(self, master)
        gui_module.frame_crime_area(self) # 범죄 지역 화면
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


# 예방 방법 버튼 눌렀을 때 뜨는 페이지
class prevention(tk.Frame):
    def __init__(self, master):
        app.geometry("500x650")
        tk.Frame.__init__(self, master)
        # 메인페이지 인증 문구
        tk.Label(self, text="범죄 예방", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        # 국가 확인 버튼
        tk.Button(self, text="국가", height = 3, width = 20,
                  command=lambda: master.switch_frame(Country)).pack(pady=5)
        # 범죄 지역 확인 버튼
        tk.Button(self, text="사회", height = 3, width = 20,
                  command=lambda: master.switch_frame(Social)).pack(pady=5)
        # 개인 방법 버튼
        tk.Button(self, text="개인", height = 3, width = 20,
                  command=lambda: master.switch_frame(individual)).pack(pady=5)
        # 메인 화면으로 돌아가기 버튼
        tk.Button(self, text="Back to main", height = 3, width = 20,
                  command=lambda: master.switch_frame(StartPage)).pack(pady=5)

# 국가 버튼 눌렀을때 뜨는 페이지
class Country(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,width=200, height=200)
        
        
        def change_img(*args) :
            state = options.get()
            if state =='First':
                l2.config(text=state)
                pLabel.config(image=self.photos[0])
                pLabel2.config(text=self.pl2txt[0])
                pLabel3.config(text=self.pl3txt[0])
                pLabel4.config(text=self.pl4txt[0])
            elif state == 'Second':
                l2.config(text=state)
                pLabel.config(image=self.photos[1])
                pLabel2.config(text=self.pl2txt[1])
                pLabel3.config(text=self.pl3txt[1])
                pLabel4.config(text=self.pl4txt[1])
            else :
                l2.config(text=state)
                pLabel.config(image=self.photos[2])
                pLabel2.config(text=self.pl2txt[2])
                pLabel3.config(text=self.pl3txt[2])
                pLabel4.config(text=self.pl4txt[2])
          

        l3 = tk.Label(self, text='Select One : ', width=10 )  
        l3.grid(row=0,column=0)

        my_list = ["First","Second","Third"]
        options = tk.StringVar(self)
        options.set(my_list[0]) # default value
        options.trace("w",change_img)
        om1 =tk.OptionMenu(self, options, *my_list)
        om1.config(width=20)
        om1.grid(row=1,column=0,columnspan=2)

        str_out='First'
        l2 = tk.Label(self,  text=str_out, width=5 )  
        l2.grid(row=0,column=1) 


        images = (Image.open('./images/국가_범죄.png'),
                    Image.open('./images/국가_청소년.png'),
                    Image.open('./images/국가_약자_아동.png'))
        images = (images[0].resize((200,200)),images[1].resize((200,200)),images[2].resize((200,200)))
        self.photos =(ImageTk.PhotoImage(images[0]),
                        ImageTk.PhotoImage(images[1]),
                        ImageTk.PhotoImage(images[2]))  
        
        self.pl2txt = ["흉악범죄 대응 강화",
                        "소년범죄 종합대책 수립",
                        '사회적 약자 대상 범죄 근절']
        self.pl3txt = ["1) 전자감독제 운영",
                        '1) 촉법소년 연령 기준 현실화',
                        '1) 아동학대 방지 전방위 시스템 구축']
        self.pl4txt = ["2) 재범 위험성 높은 강력범죄자에 대한 '보호수용 조건부 가석방'",
                        "2) 소년원 샹활실 소규모화, 소년분류심사원 확충",
                        "2)'사회적 약자 범죄 전담 수사부' 설치"]

        pLabel = tk.Label(self)
        
        pLabel.config(image=self.photos[0])
        pLabel.grid(row=2,column=0,columnspan=2)

        pLabel2 = tk.Label(self, text = self.pl2txt[0])
        pLabel2.grid(row=3 ,column=0,columnspan=2)
        pLabel3 = tk.Label(self, text = self.pl3txt[0])
        pLabel3.grid(row=4,column=0,columnspan=2)
        pLabel4 = tk.Label(self, text = self.pl4txt[0])
        pLabel4.grid(row=5,column=0,columnspan=2)
        
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(prevention)).grid(row=6,column=0 ,columnspan=2)

           
# 사회 버튼 눌렀을 때 뜨는 페이지
class Social(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,width=200, height=200)
        def change_img(*args) :
            state = options.get()
            if state =='First':
                l2.config(text=state)
                pLabel.config(image=self.photos[0])
                pLabel2.config(text=self.pl2txt[0])
            elif state == 'Second':
                l2.config(text=state)
                pLabel.config(image=self.photos[1])
                pLabel2.config(text=self.pl2txt[1])
            else :
                l2.config(text=state)
                pLabel.config(image=self.photos[2])
                pLabel2.config(text=self.pl2txt[2])
                
          

        l3 = tk.Label(self, text='Select One : ', width=10 )  
        l3.grid(row=0,column=0)

        my_list = ["First","Second","Third"]
        options = tk.StringVar(self)
        options.set(my_list[0]) # default value
        options.trace("w",change_img)
        om1 =tk.OptionMenu(self, options, *my_list)
        om1.config(width=20)
        om1.grid(row=1,column=0,columnspan=2)

        str_out='First'
        l2 = tk.Label(self,  text=str_out, width=5 )  
        l2.grid(row=0,column=1) 


        images = (Image.open('./images/사회_인프라.png'),
                    Image.open('./images/사회_데이트.png'),
                    Image.open('./images/사회_여성.png'))
        images = (images[0].resize((200,200)),images[1].resize((200,200)),images[2].resize((200,200)))
        self.photos =(ImageTk.PhotoImage(images[0]),
                        ImageTk.PhotoImage(images[1]),
                        ImageTk.PhotoImage(images[2]))  
        
        self.pl2txt = ["환경 개선: 지속 가능한 지역 범죄예방 인프라 구축",
                        "데이트 폭력 사건에 대한 대응 능력 강화를 위해 112 신고 시스템에 \n'데이트 폭력 코드'를 신설하여 출동 경찰관에게 데이트 폭력 사건임을\n 미리 인지시켜 대비할 수 있도록 함",
                        '여성 안심 귀가 서비스']
        

        pLabel = tk.Label(self)
        
        pLabel.config(image=self.photos[0])
        pLabel.grid(row=2,column=0,columnspan=2)

        pLabel2 = tk.Label(self, text = self.pl2txt[0])
        pLabel2.grid(row=3 ,column=0,columnspan=2)
        
        
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(prevention)).grid(row=6,column=0 ,columnspan=2)

# 개인 버튼 눌렀을 때 뜨는 페이지
class individual(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,width=200, height=200)
        def change_img(*args) :
            state = options.get()
            if state =='First':
                l2.config(text=state)
                pLabel.config(image=self.photos[0])
                pLabel2.config(text=self.pl2txt[0])
            elif state == 'Second':
                l2.config(text=state)
                pLabel.config(image=self.photos[1])
                pLabel2.config(text=self.pl2txt[1])
            else :
                l2.config(text=state)
                pLabel.config(image=self.photos[2])
                pLabel2.config(text=self.pl2txt[2])
                
          

        l3 = tk.Label(self, text='Select One : ', width=10 )  
        l3.grid(row=0,column=0)

        my_list = ["First","Second","Third"]
        options = tk.StringVar(self)
        options.set(my_list[0]) # default value
        options.trace("w",change_img)
        om1 =tk.OptionMenu(self, options, *my_list)
        om1.config(width=20)
        om1.grid(row=1,column=0,columnspan=2)

        str_out='First'
        l2 = tk.Label(self,  text=str_out, width=5 )  
        l2.grid(row=0,column=1) 


        images = (Image.open('./images/개인_우편함.png'),
                    Image.open('./images/개인_이메일 .png'),
                    Image.open('./images/taxi.png'))
        images = (images[0].resize((200,200)),images[1].resize((200,200)),images[2].resize((200,200)))
        self.photos =(ImageTk.PhotoImage(images[0]),
                        ImageTk.PhotoImage(images[1]),
                        ImageTk.PhotoImage(images[2]))  
        
        self.pl2txt = ["개인정보가 유출되기 때문에 우편함에 각종 고지서를\n 쌓아두지 않고 이메일 및 온라인 이용하기",
                        "출처가 불분명한 이메일이나 첨부파일은 열지 말고 삭제한다 => 사이버 범죄 예방",
                        '택시귀가 시 되도록 콜택시 사용하고 차량번호와 차종을\n 부모나 친구에게 전송하며 특히, 휴대폰 와이파이(Wi-Fi)와 위치(GPS)는 꼭 켜두기']
        

        pLabel = tk.Label(self)
        
        pLabel.config(image=self.photos[0])
        pLabel.grid(row=2,column=0,columnspan=2)

        pLabel2 = tk.Label(self, text = self.pl2txt[0])
        pLabel2.grid(row=3 ,column=0,columnspan=2)
        
        
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(prevention)).grid(row=6,column=0 ,columnspan=2)
       

# 퀴즈 변수
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
count =0


        
#퀴즈 버튼 눌렀을 때 뜨는 페이지
class Quiz(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg=BGCOLOR, width=500)
        app.geometry("500x600")
        checker = 0
        def next_question():
            global answer, index 
            
            index = index + 1
            
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
            global count
            idx = int(idx)
            if(answers[index][idx] == answers[index][4]):
                buttons[idx].config(bg=CORRECT_COLOR)
                #맞추면 자동으로 다음으로 넘어가기 (1000 = 1초)
                self.after(1000, next_question)
                count = count + 1
            else:
                buttons[idx].config(bg=WRONG_COLOR)  
        question_label = Label(self, width=40, height=2, text="test", 
                       font=("나눔바른펜", 20, "bold"), bg=BGCOLOR, fg="white")

        question_label.pack(pady = 20)   
        buttons = []
        for i in range(4):
            btn = Button(self, text=f"{i}번", width=50, height=2,
                        font=("나눔바른펜", 15, "bold"), bg=BTN_COLOR, command=lambda idx=i: check_answer(idx))
            btn.pack(pady = 10)
            buttons.append(btn)


        next_btn = Button(self, text="다음 문제", width=15, height=2,
                        command=next_question,
                        font=("나눔바른펜", 15, "bold"), bg="yellow")

        next_btn.pack(pady = 30)
    
        if checker<4:
            next_question()
            checker=checker+1
        else :
            checker=0
            pass

        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()



if __name__ == "__main__":
    app = SampleApp()
    app.geometry("500x600")
    app.mainloop()