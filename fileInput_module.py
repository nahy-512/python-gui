import csv

# 파일을 읽어들여 딕셔너리로 저장하는 함수
def readData(name):
    try:
        f = open(name, 'r', encoding='utf-8')
    except:
        print('Could not find file')
    
    data = csv.reader(f) # 파일 데이터 읽기
    next(data) # 첫째줄은 skip
    count = 0
    key = []
    value = []

    for row in data: # 한 줄씩 읽은 데이터 리스트를 key, value로 저장
        if (count == 0):
            key = row
        else:
            value = row
        count = count + 1

    mydict = dict(zip(key, value)) # 리스트를 딕셔너리로 묶기
    
    f.close
    
    return mydict   # 딕셔너리를 리턴

# 딕셔너리의 key 리스트로 변환하는 함수
def returnDictKey(dict):
    key = dict.keys()
    return key

# 딕셔너리의 value를 리스트로 변환하는 함수
def returnValue(dict):
    value = dict.values()
    #print(value)
    # for x,y in dict.items():
    #     value = y
    #     print(value)
    return value

# 딕셔너리의 key를 int로
def returnDictValue(dict):
    value = []
    #print(value)
    for x,y in dict.items():
        v = int(y)
        value.append(v)
        # print(key)
    return value 

# printKey = returnValue(readData('crime_time.csv'))
# print(printKey)