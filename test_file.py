import csv
#f = open('C://Users/nahyun/GitHub/python-gui/crime_place.txt', mode = 'r')

try:
    f = open('crime_place.txt', mode='r', encoding='utf-16')
    #f = open('crime_place.csv', 'r', encoding='utf-8')
except:
    print('Could not find file')

#lines = f.readlines()

data = csv.reader(f)
for row in data: # 한 줄씩 데이터 출력하기
    print(row) # ['서울 부산 대구 인천 광주 대전']
    for i in row:
        sp = i.split(' ') # 띄어쓰기로 구분하여 리스트 요소로 나눔
        #print(i)
    print(sp)

f.close