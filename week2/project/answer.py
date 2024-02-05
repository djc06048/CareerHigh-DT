#  데이터 받고 정제하기  (kospi200구성종목 엑셀파일, KOSPI데이터 2개 엑셀파일 Python에서 가져오기 및 데이터 정리)

import pandas as pd
import numpy as np

data = pd.ExcelFile( r"/Users/hyelim/개인공부/2024-CareerHigh-DT/study/week2/project/퀀트_Lv1_2주차_프로젝트 과제 참고자료(KOSPI200 구성종목).xlsx")
kospi200구성종목 = data.parse(0)
kospi200구성종목.index = kospi200구성종목.index.map(str)
hist_data = pd.ExcelFile(r"/Users/hyelim/개인공부/2024-CareerHigh-DT/study/week2/project/퀀트_Lv1_2주차_프로젝트 과제 참고자료(KOSPI 데이터).xlsx")
hist_price = hist_data.parse('종가')
hist_amount= hist_data.parse('거래대금')

kospi200_list = [ i[:6] for i in kospi200구성종목['종목코드'] ]


hist_price.index = hist_price.pop('일자')
hist_amount.index = hist_amount.pop('일자')
hist_price.index= hist_price.index.map(str)
hist_amount.index = hist_amount.index.map(str)
hist_price= hist_price.replace(0, np.nan)
hist_amount= hist_amount.replace(0, np.nan)
hist_price = hist_price.dropna(how='all', axis=0)
hist_amount= hist_amount.dropna(how='all', axis=0)

#%% 1. 특정일자의 kospi200종목들의 6개월 평균거래대금 dictionary 를 반환하는 함수만들기
#한달의 기준은 22영업일로 한다.

#kospi200 편입종목들의 6개월평균 거래대금 dictionary 반환
def average_amount_6m(date): #date = '20220624'  문자형식

    date_location = hist_amount.index.get_loc(date)
    temp = hist_amount.iloc[date_location-132:date_location,:].mean()
    result = {}
    for i in temp.index:
        if i in kospi200_list:
            result[i] = temp[i]
    result = sorted(result.items(), key = lambda item: item[1])
    return result

#%% 2. 2022년 6월 24일 기준 최근 6개월간 평균 거래대금이 가장 많은 20종목을 구하여라.

print(list(dict(average_amount_6m('20220624')[-20:]).keys()))

#%% 3.  해당 종목들에 동일가중 투자하였을 때 2022년6월27일 기준 수익률을 구하여라.
price_difference= hist_price.diff()
price_shift = hist_price.shift(1)
return_frame = price_difference/price_shift
port = list(dict(average_amount_6m('20220624')[-20:]).keys())

sum = 0
for i in port:
    sum+= return_frame.loc['20220627'][i]

print( sum/len(port) * 100 )
