import csv

try:
    f = open('crime_place.csv', 'r', encoding='utf-8')
except:
    print('Could not find file')

data = csv.reader(f)
next(data) # 첫째줄은 skip
count = 0
key = []
value = []

for row in data: # 한 줄씩 읽은 데이터 리스트 저장
    if (count == 0):
        key = row
    else:
        value = row
    count = count + 1
    #print(row)
    #print(row[0])

print(key)
print(value)

mydict = dict(zip(key, value)) # 리스트를 딕셔너리로 묶기
print(mydict)


f.close