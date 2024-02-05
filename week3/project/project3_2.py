import datetime

import pandas as pd

## 2. 최근 일주일간 Dataframe 2개를 자체 DB에 두개의 테이블을 만들어서 적재하기, 날짜 입력받아 해당 날짜의 종가와 거래대금 저장
closing_price = pd.ExcelFile(r"./closing_price.xlsx").parse(0)
volumn = pd.ExcelFile(r"./volumn.xlsx").parse(0)
closing_price.index = closing_price.pop(closing_price.columns[0])
volumn.index = volumn.pop(volumn.columns[0])

import sqlite3
import numpy as np

sqlite3.register_adapter(np.int64, lambda val: int(val))
conn = sqlite3.connect(r"/Users/hyelim/개인공부/2024-CareerHigh-DT/study/test.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS KOSPI200_CLOSING_PRICE (TICKER text , DATE text, LASTPRICE FLOAT)")
c.execute(
    "CREATE TABLE IF NOT EXISTS KOSPI200_TRADING_VOLUMN (TICKER text, DATE text, TRADINGAMOUNT FLOAT)")

import time

start = time.time()


list_c=[]
list_v=[]
def kospidata_to_DB(datelist):
    for idx, d in enumerate(datelist):
        ticker= closing_price.columns.tolist()
        dlist=[d]*len(ticker)
        closinglist=closing_price.iloc[idx].loc[ticker].tolist()
        volumnlist=volumn.iloc[idx].loc[ticker].tolist()
        ans_c=np.vstack((ticker,dlist,closinglist)).T
        ans_v=np.vstack((ticker,dlist,volumnlist)).T

        list_c.extend(ans_c)
        list_v.extend(ans_v)

    c.executemany("INSERT OR IGNORE INTO KOSPI200_CLOSING_PRICE VALUES (?, ?, ?)", list_c)
    c.executemany("INSERT OR IGNORE INTO KOSPI200_TRADING_VOLUMN VALUES (?, ?, ?)", list_v)

datelist = []
for date in closing_price.index:
    datelist.append(date.strftime("%Y%m%d"))

kospidata_to_DB(datelist)

print(time.time() - start)
conn.commit()
conn.close()

## db 에 넣을 때는 튜플로 만들어서 넣어야한다.  c.executemany()
## 기업에서는 res 형식으로 데이터베이스 이용

## 배치 파일로 돌아감

## 4. 상위 거래대금 20 위 공시자료 찾기
