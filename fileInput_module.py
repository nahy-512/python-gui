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
            key = row # 첫째줄을 key 리스트로 저장
        else:
            v = [] # 둘째줄을 v 리스트에 저장
            v = row
        count = count + 1
    
    for i in v: # int로 변환해서 value 저장
        value.append(int(i))
    mydict = dict(zip(key, value)) # 리스트를 딕셔너리로 묶기

    f.close
    
    return mydict   # 딕셔너리를 리턴

# 딕셔너리의 key 리스트로 변환하는 함수
def returnDictKey(dict):
    key = dict.keys()
    return key

# 딕셔너리의 value를 리스트로 변환하는 함수
def returnDictValue(dict):
    value = dict.values()

    return value

# 가장 높은 value값을 가진 key
def returnMinMax(dict):
    print("dict={}" .format(dict))
    min = 10000000; max = -1
    for x,y in dict.items():
        if (y > max):
            max = y
            maxKey = x
        if (y < min):
            min = y
            minKey = x
    myTuple = (min, max) # min, max를 튜플로 저장
    myKeyTuple = (minKey, maxKey)
    
    return myKeyTuple