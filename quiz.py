from tkinter import *
win = Tk()

def check():
    print()

# Quiz Label Index
q1 = Label(win, text='Q1) 퀴즈 1')
q2 = Label(win, text='Q2) 퀴즈 2')
q3 = Label(win, text='Q3) 퀴즈 3')
q4 = Label(win, text='Q4) 퀴즈 4')

# Question Index
g1 = StringVar()
g2 = StringVar()
g3 = StringVar()
g4 = StringVar()

# Radio Button
rdo1_1 = Radiobutton(win, text='Yes', variable=g1, value='1-1', command=check)
rdo1_2 = Radiobutton(win, text='No', variable=g1, value='1-2', command=check)

rdo2_1 = Radiobutton(win, text='Yes', variable=g2, value='2-1', command=check)
rdo2_2 = Radiobutton(win, text='No', variable=g2, value='2-2', command=check)

rdo3_1 = Radiobutton(win, text='Yes', variable=g3, value='3-1', command=check)
rdo3_2 = Radiobutton(win, text='No', variable=g3, value='3-2', command=check)

rdo4_1 = Radiobutton(win, text='Yes', variable=g4, value='4-1', command=check)
rdo4_2 = Radiobutton(win, text='No', variable=g4, value='4-2', command=check)

# set default select
rdo1_1.select; rdo2_1.select; rdo3_1.select; rdo4_1.select

q1.pack(); rdo1_1.pack(); rdo1_2.pack()
q2.pack(); rdo2_1.pack(); rdo2_2.pack()
q3.pack(); rdo3_1.pack(); rdo3_2.pack()
q4.pack(); rdo4_1.pack(); rdo4_2.pack()






win.mainloop()