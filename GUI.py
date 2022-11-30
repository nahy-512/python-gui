import tkinter

window = tkinter.Tk()
window.title("Frame_Change")
window.geometry("600x600+200+200")

frame_main = tkinter.Frame(window) # 메인 화면
frame1 = tkinter.Frame(window) # 범죄 시간대 화면
frame2 = tkinter.Frame(window) # 범죄 지역 화면
frame3 = tkinter.Frame(window) # 예방 방법 화면
frame4 = tkinter.Frame(window) # 퀴즈 화면

frame_main.grid(row=0, column=0, sticky="nsew")
frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=0, sticky="nsew")

def openFrame(frame):
    frame.tkraise()

# 메인 -> 루트 화면 전환
btnToFrame1 = tkinter.Button(frame_main,
text="Change To Frame1",
padx=10,
pady=10,
command=lambda:[openFrame(frame1)])

btnToFrame2 = tkinter.Button(frame_main,
text="Change To Frame2",
padx=10,
pady=10,
command=lambda:[openFrame(frame2)])

btnToFrame3 = tkinter.Button(frame_main,
text="Change To Frame3",
padx=10,
pady=10,
command=lambda:[openFrame(frame3)])

btnToFrame4 = tkinter.Button(frame_main,
text="Change To Frame4",
padx=10,
pady=10,
command=lambda:[openFrame(frame4)])

btnToFrame1.pack()
btnToFrame2.pack()
btnToFrame3.pack()
btnToFrame4.pack()

openFrame(frame_main) # 기본메인화면
window.mainloop()