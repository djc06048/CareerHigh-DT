import datetime

import numpy as np
import pandas as pd

KOSPI200_data = pd.ExcelFile(
    r"/Users/hyelim/개인공부/2024-CareerHigh-DT/study/week2/project/퀀트_Lv1_2주차_프로젝트 과제 참고자료(KOSPI 데이터).xlsx")
KOSPI200_classifer = pd.ExcelFile(
    r"/Users/hyelim/개인공부/2024-CareerHigh-DT/study/week2/project/퀀트_Lv1_2주차_프로젝트 과제 참고자료(KOSPI200 구성종목).xlsx")

close_price = KOSPI200_data.parse("종가")
volume = KOSPI200_data.parse("거래대금")

close_price = close_price.T
volume = volume.T

close_price.columns = close_price.iloc[0, :]
close_price = close_price.drop(index="일자")
volume.columns = volume.iloc[0, :]
volume = volume.drop(index="일자")

close_price.columns = pd.to_datetime(close_price.columns, format="%Y%m%d").date
volume.columns = pd.to_datetime(volume.columns, format="%Y%m%d").date
print(type(close_price))
from datetime import datetime
from dateutil.relativedelta import relativedelta


def average_amount_6m(date):
    end_date = datetime.strptime(date, "%Y%m%d")
    start_date = (end_date + relativedelta(days=- 132)).date()
    end_date = end_date.date()
    print(end_date, start_date)
    selected_data = volume.loc[:, start_date:end_date]
    cumsum_selected_data = np.cumsum(selected_data, axis=1)

    answer = []
    for idx, i in enumerate(cumsum_selected_data.index):
        dict = {}
        average = cumsum_selected_data.iloc[idx, -1] / 132
        dict[i] = average
        answer.append(dict)
        print(answer)
    return answer


volumn6 = average_amount_6m('20220624')

def best_volumn_top_20(volumn):
    sorted_volume = sorted(volumn, key=lambda x: list(x.values()))
    top_20 = sorted_volume[:20]

    print(top_20)

best_volumn_top_20(volumn6)
