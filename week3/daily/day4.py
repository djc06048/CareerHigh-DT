# 효율적 투자선 그리기
import numpy as np
import pandas as pd

from day2 import Return_of_Port, Volatility_Of_Port

ratios = np.arange(1, 11)
volatility_list = []
expected_return_list = []

for w1 in ratios:
    for w2 in ratios:
        for w3 in ratios:
            profit = Return_of_Port([w1, w2, w3])
            vol = Volatility_Of_Port([w1, w2, w3])

            expected_return_list.append(profit)
            volatility_list.append(np.round(vol,3))

import matplotlib.pyplot as plt

max_return_for_each_vol = []

for unique_vol in set(volatility_list):
    returns_for_unique_vol=[pair[1] for pair in zip(volatility_list, expected_return_list) if pair[0] == unique_vol]
    print(returns_for_unique_vol)
    max_return_for_each_vol.append((unique_vol,np.max(returns_for_unique_vol)))

max_return_for_each_vol.sort(key=lambda x:x[0])
print(max_return_for_each_vol)
plt.plot([pair[0] for pair in max_return_for_each_vol],[pair[1] for pair in max_return_for_each_vol],c='r',label='Efficient Frontier')
plt.scatter(volatility_list, expected_return_list, c='b', marker='o',label='All Portfolios')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.title('Portfolio Optimization')
plt.legend()
plt.show()


