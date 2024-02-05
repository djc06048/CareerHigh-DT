## 테이블 초기화
import sqlite3

#
conn = sqlite3.connect(r"../../test.db", isolation_level=None)
c = conn.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS KOSPI200 (tickers text PRIMARY KEY, full_name text,"
#           "market_cap integer, Lastprice integer)")
# import pandas as pd
#
# data = pd.ExcelFile(r"../../3364.xlsx")
# data = data.parse(0)
#
# input_data = []
# for i in data.index:
#     temp = data.loc[i, ["종목코드", "종목명", "상장시가총액", "종가"]].tolist()
#     temp[2:] = list(map(int, temp[2:]))
#     input_data.append(tuple(temp))
#
# print(input_data)
# input_data = tuple(input_data)
# c.executemany("INSERT INTO KOSPI200(tickers,full_name, market_cap,Lastprice) VALUES(?,?,?,?)", input_data)

c.execute("SELECT * FROM KOSPI200")
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())

c.execute("SELECT * FROM KOSPI200")
print(c.fetchall())

c.execute("SELECT * FROM KOSPI200")
for row in c.fetchall():
    print(row)

## pandas로 데이터 끌어오는 방식
import pandas as pd

temp_table = pd.read_sql_query("select * from KOSPI200", conn)
print(temp_table)

c.execute("SELECT K.tickers 티커 FROM KOSPI200 as K")
temp_table = pd.read_sql_query("SELECT K.tickers 티커 FROM KOSPI200 as K", conn)
print(temp_table)

param4 = ('005930 KS Equity', '000660 KS Equity')
c.execute('SELECT * FROM KOSPI200 WHERE tickers IN(?,?)', param4)
print(param4, c.fetchall())

## 삭제, 수정

c.execute("UPDATE KOSPI200 SET full_name='SAMSUNG_ELECTRONICS' WHERE tickers='005930 KS Equity'")
c.execute("UPDATE KOSPI200 SET full_name=? WHERE tickers=?", ('LG_ENERGYSOLUTION', '373220 KS Equity'))

c.execute("SELECT * FROM KOSPI200")
print(c.fetchone())
print(c.fetchone())

## 복수 삭제
c.execute("DELETE FROM KOSPI200 WHERE tickers IN ('005930 KS Equity','373220 KS Equity')")

c.close() ## -> 동시 작업 위해 연결해제가 필수
conn.close()


conn = sqlite3.connect(r"../../test.db", isolation_level=None)
c = conn.cursor()

with conn:
    for line in conn.iterdump():
        print(line)

with conn:
    with open(r"../../dump.sql","w") as f:
        for line in conn.iterdump():
            f.write("%s\n" %line)
