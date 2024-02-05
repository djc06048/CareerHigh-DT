import pandas as pd

data = pd.ExcelFile(r"/Users/hyelim/개인공부/2024-CareerHigh-DT/study/week2/모의면접/parkingdata_1.xlsx")
parkingdata = data.parse("입출차기록")
staffdata = data.parse("입주사차량")

parkingdata.index = parkingdata.pop("시간")

from datetime import datetime

summary = dict()
car_set = set()

for i in parkingdata.index:
    if parkingdata.loc[i, '차번호'] in car_set:
        summary[parkingdata.loc[i, '차번호']].append(i)
    else:
        summary[parkingdata.loc[i, '차번호']] = [i]
    car_set.add(parkingdata.loc[i, '차번호'])
result = {}

for i in summary.keys():
    fee = []
    temp = summary[i]

    if len(temp) % 2 == 1:
        fee.append(30000)
        temp = temp[:-1]
    for j in range(int(len(temp) / 2)):
        time = (datetime.strptime(temp[2 * j + 1], "%H:%M:%S") - datetime.strptime(temp[2 * j],
                                                                                   "%H:%M:%S")).total_seconds()
        fee.append(min((time // 600) * 1000, 12000))

    if len(fee) > 3:
        fee.remove(min(fee))
    fee_sum = sum(fee)

    if i in list(staffdata.iloc[:,0]):
        fee_sum *= 0.5
    result[i] = fee_sum
print(sum(result.values()))
