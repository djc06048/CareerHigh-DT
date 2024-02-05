# (0,0.025)와 선 그었을 경우 기울기가 가장 큰 점의 포트폴리오 정보값을 구하고, 해당
# 포트폴리오를 구성하기 위한 비율을 구하고, 아래와 같이 그림으로 표현하기
import numpy as np

from day2 import Return_of_Port, Volatility_Of_Port

ratios = np.arange(1, 11)
volatility_list = []
expected_return_list = []

## 3일차 : 변동성, 기대 수익률 구하기
for w1 in ratios:
    for w2 in ratios:
        for w3 in ratios:
            profit = Return_of_Port([w1, w2, w3])
            vol = Volatility_Of_Port([w1, w2, w3])

            expected_return_list.append(profit)
            volatility_list.append(np.round(vol, 3))

# 4일차 :  Efficient Frontier 구하기
max_return_for_each_vol = []

for unique_vol in set(volatility_list):
    returns_for_unique_vol = [pair[1] for pair in zip(volatility_list, expected_return_list) if pair[0] == unique_vol]
    print(returns_for_unique_vol)
    max_return_for_each_vol.append((unique_vol, np.max(returns_for_unique_vol)))

max_return_for_each_vol.sort(key=lambda x: x[0])
print(max_return_for_each_vol)

# 5일차: 타겟포인트 기준 최대의 기울기를 가지는 포트폴리오 정보(변동성, 기대수익률)  구하기
target_point = np.array([0, 0.025])
max_slope = float('-inf')
max_slope_point = None
slope = None
for i in range(len(volatility_list)):
    x_diff = volatility_list[i] - target_point[0]
    y_diff = expected_return_list[i] - target_point[1]

    if x_diff != 0:
        slope = y_diff / x_diff
    if slope > max_slope:
        max_slope_point = (volatility_list[i], expected_return_list[i])
        max_slope = slope
import matplotlib.pyplot as plt
plt.xlim(0.00, 0.14)
plt.ylim(0.01, 0.04)
plt.scatter(volatility_list, expected_return_list, c='b', marker='o', label='All Portfolios')

plt.plot([max_slope_point[0], target_point[0]], [max_slope_point[1], target_point[1]], c='g', marker='d',
         label='Max Slope line')
plt.plot([pair[0] for pair in max_return_for_each_vol], [pair[1] for pair in max_return_for_each_vol], c='r',
         label='Efficient Frontier')

plt.xlabel('Volatility')
plt.ylabel('Return')
plt.title('Portfolio Optimization')
plt.legend()
plt.show()
