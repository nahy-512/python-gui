from tkinter import*
import matplotlib.pyplot as plt
import fileInput_module

# 범죄 시간 테스트
# dict = fileInput_module.readData('crime_time_cp.csv')
# 범죄 지역 테스트
dict = fileInput_module.readData('crime_area_csv')

print(dict)
key = fileInput_module.returnDictKey(dict)
value = fileInput_module.returnDictValue(dict)
print(value)

plt.plot(key, value)
# plt.plot(range(1,len(value)+1), value, color='b', linewidth=2, label="cirme time")
plt.title('Crime Time') # 제목
plt.grid(True) # 그리드
plt.xlabel('time', labelpad=25)
plt.ylabel('value')
plt.legend()
    
plt.show()
