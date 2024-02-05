import pandas as pd

# 데이터 전처리
data = pd.ExcelFile(r"/Users/hyelim/개인공부/2024-CareerHigh-DT/study/week1/project/퀀트_Lv1_1주차_프로젝트 과제 참고자료 (1).xlsx")
data = data.parse(0)

data.index = data.pop(data.columns[0])
data = data.drop(index="Date")
data.columns = data.iloc[0, :]  # 0번째행의 모든 열

data.index.names = ['Date']
data = data.iloc[1:, :]
print(data)

# 수익률 프레임 만들기
import numpy as np

# log(x)=x-1
# x=1 근처임, 대부분의 수익률(오눌/전날) 은 1근처 -> 금융에서 로그 수익률을 많이 사용함

log_frame = np.log(data.astype(float))
return_frame = log_frame.diff()
return_frame = return_frame.dropna()

# 일반적인 수익률 프레임 만들기, 수익률: (오늘주가-전날주가)/전날 주가

price_difference = data.diff()
price_shift = data.shift(1)
return_frame = price_difference / price_shift
print(return_frame)

return_frame = return_frame.dropna(axis=0)
print(return_frame)

# 2022-05-27 일자를 받아서 해당 일자의 종목-수익률 dictionary 구성
import datetime

date_for_research = input("원하시는 날짜를 입력해주세요 ex 2023-05-27 : ")
date_for_research = datetime.datetime.strptime(date_for_research, "%Y-%m-%d")
daily_return = dict(return_frame.loc[date_for_research, :])
sorted_dict = sorted(daily_return.items(), key=lambda item: item[1])
print(sorted_dict)

winner = dict(sorted_dict[-10:])
loser = dict(sorted_dict[:10])

import numpy as np

# 주간 5영업일, 월간 22영업일, 연간 252영업일

기준일자인덱스 = return_frame.index.get_loc(date_for_research)
week_ago = return_frame.index[기준일자인덱스 - 5]
month_ago = return_frame.index[기준일자인덱스 - 22]
year_ago = return_frame.index[기준일자인덱스 - 252]

# 주가, 수익률
# 수익률 가지고 누적 수익률 구하는 과정
# 0.01 0.02 0.03(3%)
# ->(1.01)*(1.02)*(1.03)-1

weekly_ret = (return_frame.iloc[기준일자인덱스 - 4:기준일자인덱스 + 1, :] + 1).cumprod().iloc[-1, :] - 1  # 가장 마지막 날짜
monthly_ret = (return_frame.iloc[기준일자인덱스 - 21:기준일자인덱스 + 1, :] + 1).cumprod().iloc[-1, :] - 1  # 가장 마지막 날짜
yearly_ret = (return_frame.iloc[기준일자인덱스 - 251:기준일자인덱스 + 1, :] + 1).cumprod().iloc[-1, :] - 1  # 가장 마지막 날짜

# 변동성
# 주식의 변동성: 특정 주식의 일간 수익률의 표준편차의 연율화
# - 주가의 표준편차가 아님, 주가의 표준편차는 종목별로 다르다.
# 종목들의 수익률의 표준편차가 종목의 변동성
# 금리 등 금융권에서는 연율화를 쓴다.

# 변동성 - 첫날 기준으로 +- 변동성 부분에 들어올 확률이 원시그마이다(68.2%)

std_dev = return_frame.iloc[기준일자인덱스 - 251:, :].std() * np.sqrt(252)

winner_table = pd.DataFrame(index=["주간수익률", "월간수익률", "연간수익률", "연간변동성"], columns=winner.keys())
loser_table = pd.DataFrame(index=["주간수익률", "월간수익률", "연간수익률", "연간변동성"], columns=loser.keys())

for i in winner_table.columns:
    winner_table.loc["주간수익률", i] = weekly_ret[i]
    winner_table.loc["월간수익률", i] = monthly_ret[i]
    winner_table.loc["연간수익률", i] = yearly_ret[i]
    winner_table.loc["연간변동성", i] = std_dev[i]

for i in loser_table.columns:
    loser_table.loc["주간수익률", i] = weekly_ret[i]
    loser_table.loc["월간수익률", i] = monthly_ret[i]
    loser_table.loc["연간수익률", i] = yearly_ret[i]
    loser_table.loc["연간변동성", i] = std_dev[i]

writer = pd.ExcelWriter(r"/Users/hyelim/개인공부/2024-CareerHigh-DT/study/week1/project/answer_result.xlsx", engine='xlsxwriter')
winner_table.to_excel(writer, sheet_name="Winner")
loser_table.to_excel(writer, sheet_name="Loser")
writer.close()
