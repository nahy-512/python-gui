from tkinter import*
import matplotlib.pyplot as plt
import pickle
import fileInput_module

# win = Tk()
# win.title('Subframe test')
# win.geometry('600x600+200+200')

def drawPlot(name):
    # matplotlib
    print('Button Click')
    dict = fileInput_module.readData(name) # 'crime_time_cp.csv'
    print(dict)
    key = fileInput_module.returnDictKey(dict)
    value = fileInput_module.returnDictValue(dict)
    print(value)

    plt.plot(key, value)
    # plt.plot(range(1,len(value)+1), value, color='b', linewidth=2, label="cirme time")
    plt.title('Crime Time') # 제목
    plt.grid(True) # 그리드
    plt.xlabel('time')
    plt.ylabel('value')
    plt.legend()
    
    plt.show()

def goToChart():
    # matplotlib
    print('Button Click')
    dict = fileInput_module.readData('crime_time_cp.csv') # 'crime_time_cp.csv'
    print(dict)
    key = fileInput_module.returnDictKey(dict)
    value = fileInput_module.returnDictValue(dict)
    print(value)

    plt.plot(key, value)
    # plt.plot(range(1,len(value)+1), value, color='b', linewidth=2, label="cirme time")
    plt.title('Crime Time') # 제목
    plt.grid(True) # 그리드
    plt.xlabel('time')
    plt.ylabel('value')
    plt.legend()
    
    plt.show()


def frame_crime_time(name): # name: frame name
    print("Crime Time Frame")
    lb = Label(name, text='Crime Time', font=('Helvetica', 25))
    lb.pack()

    dict = fileInput_module.readData('crime_time.csv') # 파일을 읽어들여서 받은 딕셔너리
    result = pickle.dumps(dict) # 딕셔너리를 스트링으로 변환
    #returns = pickle.loads(result)
    #print(returns)

    lb2 = Label(name, text=result) # 데이터 테스트용 라벨
    lb2.pack()
    
    plotBtn = Button(name, text='차트 바로가기', command=goToChart) # drawPlot('crime_time_cp.csv')
    plotBtn.pack()


def frame_cirme_area(name):
    print("Crime Area Frame")
    lb = Label(name, text='Crime Area', font=('Helvetica', 25))
    lb.pack()

    dict = fileInput_module.readData('crime_area.csv') # 파일을 읽어들여서 받은 딕셔너리
    result = pickle.dumps(dict) # 딕셔너리를 스트링으로 변환
    #returns = pickle.loads(result)
    #print(returns)

    lb2 = Label(name, text=result) # 데이터 테스트용 라벨
    lb2.pack()
    
    plotBtn = Button(name, text='차트 바로가기', bg='green', fg='black', command=drawPlot('crime_area_cp.csv'))
    plotBtn.pack()

# frame_crime_time(win)
# win.mainloop()