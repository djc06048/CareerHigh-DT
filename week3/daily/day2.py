#2 원하는 수식 표현하기(기초 투자론)

import numpy as np
cov = np.array([[0.018, 0.002, -0.01], [0.002, 0.03, 0.002], [-0.01, 0.002, 0.016]])
ret=np.array([0.03,0.04,0.02])

def Return_of_Port(w):
    weights = np.array(w,dtype=float)
    weights /= np.sum(weights) # 정규화
    return np.dot(weights,ret) # 행렬의 곱 - 열과 행이 같아야하지만 파이썬 내부로 전치 시켜준다.
print("기대수익률", Return_of_Port([1,2,3]))


# [w1,w2,w3]  ([[b1,s12,s13],   w1
#               [s12,b2,s23],   w2
#               s13,s23,b3])    w3
def Volatility_Of_Port(w):
    weights = np.array(w,dtype=float)
    weights /= np.sum(weights)
    res = np.dot(weights, np.dot(cov, weights))
    return np.sqrt(res)
print("포트폴리오 변동성:", Volatility_Of_Port([1,2,3]))




# 자산간의 상관계수가 음수이면 포트폴리오의 변동성이 낮아진다. - 햇지 투자 ( 서로 다른 방향성을 가진 자산을 투자하는 방식)
# w가 정해지면 포트폴리오의 수익률과 변동성을 구할 수 있다.
