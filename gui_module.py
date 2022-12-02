from tkinter import*
import matplotlib.pyplot as plt
import fileInput_module

def goToTimeChart(): # 범죄 시간대 차트 그리기
    # matplotlib
    print('Button Click')
    dict = fileInput_module.readData('crime_time.csv')
    print(dict)
    key = fileInput_module.returnDictKey(dict)
    value = fileInput_module.returnDictValue(dict)
    print(value)

    plt.plot(key, value)
    plt.title('Crime Time Chart') # 제목
    plt.grid(True) # 그리드
    plt.xlabel('time')
    plt.ylabel('value')
    plt.legend()
    
    plt.show()

def goToAreaChart(): # 범죄 지역 차트 그리기
    # matplotlib
    print('Button Click')
    dict = fileInput_module.readData('crime_area.csv')
    print(dict)
    key = fileInput_module.returnDictKey(dict)
    value = fileInput_module.returnDictValue(dict)
    print(value)

    plt.scatter(key, value)
    plt.title('Crime Area Chart') # 제목
    plt.grid(True) # 그리드
    plt.xlabel('area')
    plt.ylabel('value')
    plt.legend()
    
    plt.show()

# 범죄 시간대 화면
def frame_crime_time(name): # name: frame name
    print("Crime Time Frame")
    titleLb = Label(name, text='Crime Time\n', font=('Helvetica', 25)) # 제목
    titleLb.pack()

    dict = fileInput_module.readData('crime_time.csv') # 파일을 읽어들여서 받은 딕셔너리
 
    minKey, maxKey = fileInput_module.returnMinMax(dict) # 튜플 언패킹
    print("min={}, max={}" .format(min, max))
    minLb = Label(name, text='범죄가 가장 적게 발생한 시간대: {}시\n범죄 건수: {}(건)' .format(minKey, dict[minKey]))
    maxLb = Label(name, text='범죄가 가장 많이 발생한 시간대: {}시\n범죄 건수: {}(건)' .format(maxKey, dict[maxKey]) ) 

    maxLb.pack()
    minLb.pack()
    
    plotBtn = Button(name, text='차트 바로가기', command=goToTimeChart) # drawPlot('crime_time_cp.csv')
    plotBtn.pack()

# 범죄 지역 화면
def frame_cirme_area(name):
    print("Crime Area Frame")
    titleLb = Label(name, text='Crime Area\n', font=('Helvetica', 25))
    titleLb.pack()

    dict = fileInput_module.readData('crime_area.csv') # 파일을 읽어들여서 받은 딕셔너리

    minKey, maxKey = fileInput_module.returnMinMax(dict) # 튜플 언패킹
    minLb = Label(name, text='범죄가 가장 적게 발생한 지역: {}\n범죄 건수: {}(건)' .format(minKey, dict[minKey]))
    maxLb = Label(name, text='범죄가 많이 적게 발생한 지역: {}\n범죄 건수: {}(건)' .format(maxKey, dict[maxKey]))

    maxLb.pack()
    minLb.pack()
    
    plotBtn = Button(name, text='차트 바로가기', command=goToAreaChart)
    plotBtn.pack()
