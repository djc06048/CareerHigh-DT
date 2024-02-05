import numpy as np

from day2 import Return_of_Port, Volatility_Of_Port

# 3 모든 비율 경우의 수에 대해, 결과자료 scatter 로 나타내기
# 변동성 - 위험(x), 수익률 - 수익(y)
ratios = np.arange(1, 11)
volatility_list = []
expected_return_list = []

for w1 in ratios:
    for w2 in ratios:
        for w3 in ratios:
            profit = Return_of_Port([w1, w2, w3])
            vol = Volatility_Of_Port([w1, w2, w3])

            expected_return_list.append(profit)
            volatility_list.append(vol)

import matplotlib.pyplot as plt

plt.scatter(volatility_list, expected_return_list, c='b', marker='o',label='All Portfolios')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.title('Portfolio Optimization')
plt.legend()
plt.show()







