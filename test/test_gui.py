import tkinter
import gui_module
#import matplotlib

try:
    import tkinter as tk
except:
    import tkinter as tk

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
        tk.Label(self, text="범죄율 분석", font=('Helvetica', 20, "bold")).pack(side="top", fill="x", pady=5)
        # 범죄 시간대 확인 버튼
        tk.Button(self, text="범죄 시간대 확인",
                  command=lambda: master.switch_frame(crime_time_zone),
                  anchor="center", height = 3, width = 20, relief="ridge",
                  activebackground='#cccccc', 
                  cursor="target").pack(pady=5)
        # 범죄 지역 확인 버튼
        tk.Button(self, text="범죄 지역 확인",
                  command=lambda: master.switch_frame(crime_area),
                  anchor="center", height = 3, width = 20,relief="ridge",
                  activebackground='#cccccc', cursor="target").pack(pady=5)
        # 예방방법 버튼
        tk.Button(self, text="예방 방법",
                  command=lambda: master.switch_frame(prevention),
                  anchor="center", height = 3, width = 20, relief="ridge",
                  activebackground='#cccccc', cursor="target").pack(pady=5)
        # 퀴즈 버튼
        tk.Button(self, text="퀴즈",
                  command=lambda: master.switch_frame(Quiz),
                  anchor="center", height = 3, width = 20, relief="ridge",
                  activebackground='#cccccc', cursor="target").pack(pady=5)

#범죄 시간 확인 버튼 눌렀을때 뜨는 페이지
class crime_time_zone(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage),
                  anchor="center", width = 17, relief="ridge",
                  activebackground='#cccccc', cursor="target").pack()
        tk.Label(width=1)
        gui_module.frame_crime_time(self) # 범죄 시간 화면

#범죄 지역 확인 버튼 눌렀을 때 뜨는 페이지
class crime_area(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage),
                  anchor="center", width = 17, relief="ridge",
                  activebackground='#cccccc', cursor="target").pack()
        gui_module.frame_cirme_area(self) # 범죄 지역 화면

#예방 방법 버튼 눌렀을 때 뜨는 페이지
class prevention(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage),
                  anchor="center", width = 17, relief="ridge",
                  activebackground='#cccccc', cursor="target").pack()
        
        
#퀴즈 버튼 눌렀을 때 뜨는 페이지
class Quiz(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage),
                  anchor="center", width = 17, relief="ridge",
                  activebackground='#cccccc', cursor="target").pack()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("300x350")
    app.resizable(True, True)
    app.title("Group 4")
    app.mainloop()