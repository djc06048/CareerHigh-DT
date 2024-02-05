from factoral_module import facto
print(facto(5))

import time
print(time.time())
print(time.localtime(time.time()))
print(time.strftime("%Y-%m-%d",time.localtime(time.time()))) # 시간 객체를 원하는 형태로 출력
print(time.strftime("%c",time.localtime(time.time())))

import datetime
print(datetime.datetime.today())

date=datetime.datetime.strptime('2021-01-02','%Y-%m-%d') # 문자열로 시간객체 생성
print(date,"시간 객체 생성")

print(date.strftime("%Y-%m-%d"))

date=datetime.datetime.today()
print(date.year, date.month, date.day, date.hour, date.minute, date.second, date.microsecond)

day1=datetime.timedelta(days=1)
print(day1+date)

week1=datetime.timedelta(weeks=1)
print(week1+date)

import math
print(math.sqrt(4))

import random
print(random.random())
print(random.uniform(1,10))
print(random.randint(1,10))
print(random.randrange(0,101,2))
print(random.normalvariate(0,1))

import numpy as np
a=[1,2,3]
b=np.array(a)
print(b)
a=[[1,2,3],[4,5,6]]
b=np.array(a)
print(b.shape)

print(np.arange(10))
print(np.arange(5,10))

print(np.zeros((2,2)))
print(np.ones((2,3)))
print(np.full((2, 3),100))
print(np.eye(3))

import pandas as pd
data={
    'year':[2020,2021,2022],
    '철수성적':[95,100,70],
    '영희성적':[80,90,100]
}
print(data)
df=pd.DataFrame(data,index=data['year'])
print(df)
# df.to_excel(r"/Users/hyelim/개인공부/2024-CareerHigh-DT/study/week1/연습엑셀.xlsx")
test=pd.ExcelFile(r"/week1/연습엑셀.xlsx")
print(test)
df= test.parse(0) #0 번째 시트
print(df)
df.index=["20","21","22","23"]
df=pd.DataFrame(data,index=data['year'])
print(df)
print(df.index)
print(df.columns)
print(df.head())
print(df.loc[2020,['철수성적']])
print(df.iloc[1:,1])
print(df.describe())

import matplotlib.pyplot as plt
# plt.plot([100,50,0,200,50,300])
# plt.show()
#
# plt.plot([20,21,22],[95,100,70])
# plt.show()
#
# plt.plot([20,21,22],[95,100,70],'ro')
# plt.axis([19,23,50,110])
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd
data={
    'year':[2020,2021,2022],
    '철수성적':[95,100,70],
    '영희성적':[80,90,100]
}
df=pd.DataFrame(data,index=data.pop('year'))
print(df)
plt.plot(df['철수성적'],'r')
plt.plot(df['영희성적'],'b')
plt.axis([2020,2022,50,150])
plt.xticks([2020,2021,2022])
plt.legend(['chulsoo','younghee'])
plt.xlabel('Year')
plt.ylabel('Score')
plt.show()
