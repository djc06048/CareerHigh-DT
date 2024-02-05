#2 원하는 수식 표현하기 (기초 투자론)
import numpy as np

ret = [0.01, 0.04,0.03]
cov = np.array([[0.018,0.002,-0.01],[0.002,0.03,0.002],[-0.01,0.002,0.016]])
def Return_Of_Port(w): #w=[1,2,3]
    w = np.array(w)/sum(w)
    return np.dot(w,np.array(ret))

print(Return_Of_Port([1,2,3]))

def Volatility_Of_Port(w): #w=[1,2,3]
    w = np.array(w)/sum(w)
    res = np.dot(np.dot(w,cov),w)
    return np.sqrt(res)

print(Volatility_Of_Port([1,2,3]))

#3 모든 비율 경우의수에 대하여, 결과자료 scatter로 나타내기
return_list=[]
volatility_list=[]
weight_list=[]
[weight_list.append([i,j,k]) for k in range(1,11) for j in range(1,11) for i in range(1,11)]

for w in weight_list:
    return_list.append(Return_Of_Port(w))
    volatility_list.append(Volatility_Of_Port(w))
import matplotlib.pyplot as plt
plt.xlim(0.05,0.14)
plt.ylim(0.01,0.04)
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.title('Portfolio Optimization')
plt.scatter(volatility_list,return_list,s=1)

#4 Efficient Frontier 그리기

# 같은 변동성 or 같은 수익률 하에는 판단 가능
# 판단 불가능한 것들이 효율적 투자선 : 수익률을 높여가며 표준편차가 최소인 지점들의 집합


VR_array = np.vstack((np.array(volatility_list),np.array(return_list)))

EF_vol = [min(volatility_list)]
EF_ret = [return_list[np.argmin(volatility_list)]]

for v in np.linspace(0.05,0.14,num=10):
    temp = np.where((VR_array[0,:]>v) &( VR_array[0,:]<v+0.01),VR_array,0 ) #변동성 구간을 정해서 그 구간안의 표본만 활성화
    ind = np.argmax(temp,axis=1)[1] #수익률이 가장 높은 인덱스위치 반환
    EF_vol.append(temp[0,ind])
    EF_ret.append(temp[1,ind])

import matplotlib.pyplot as plt
plt.xlim(0.05, 0.14)
plt.ylim(0.01, 0.04)
plt.xlabel("Volatility")
plt.ylabel("Return")
plt.scatter(volatility_list, return_list,s=1)
plt.plot(EF_vol,EF_ret,color='r')

plt.show()

## 5. sharpe ratio maximize 하기
# 예금 대비 어느정도로 수익률을 받나? 내가 가지고 있는 위험 대비
# 위험을 가지고 있는 대비 얼마나 수익을 얻냐 -> 샤프비율
# (포트폴리오 수익률 - 무위험자산수익률)/ 변동성 = 초과수익률/변동성
# 무위험 자산 수익률 - 0.025 (예금)과 주식 포트폴리오 red 위의 점 선택
# 기울기 - 샤프 비율 ( 초과수익률(y축) /변동성(x축))
# 효율적 투자선의 접선에 존재한다. 그 선에서는 어떤 걸 투자해도 된다. 종목 투자 비율만 달라짐


def slope(p1,p2): #p1점과 p2점의 기울기를 반환.
    arr = np.array(p2)-np.array(p1)
    return arr[1]/arr[0]

return_list = []
volatility_list = []
weight_list = []
slope_list = []

[weight_list.append([i,j,k]) for k in range(1,11) for j in range(1,11) for i in range(1,11)]

for w in weight_list:
    return_value = Return_Of_Port(w)
    vol_value = Volatility_Of_Port(w)
    return_list.append(return_value)
    volatility_list.append(vol_value )
    slope_list.append(slope([0,0.025],[vol_value,return_value]))

maximize_index = np.argmax(slope_list)
print ("(volatility,return)is (",volatility_list[maximize_index] , return_list[maximize_index] , ")")
print("weight is ",weight_list[maximize_index])

import matplotlib.pyplot as plt
plt.xlim(0.00, 0.14)
plt.ylim(0.01, 0.04)
plt.xlabel("Volatility")
plt.ylabel("Return")
plt.scatter(volatility_list, return_list,s=1)
plt.plot(EF_vol,EF_ret,color='r')


plt.plot(volatility_list[maximize_index], return_list[maximize_index], marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")
plt.plot(0, 0.025, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")
plt.plot([0,volatility_list[maximize_index]],[0.025, return_list[maximize_index]],color="black")
plt.show()

# 주식 포트폴리오 완성!
