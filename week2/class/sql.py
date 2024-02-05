import sqlite3

# print(sqlite3.version)
# conn = sqlite3.connect(r"../test.db")
# c = conn.cursor()
# c.execute("CREATE TABLE test_table_1 (test text)")
# conn.commit()
# c.close()
# conn.close()

## DB 생성 - auto commit
conn = sqlite3.connect(r"../../test.db", isolation_level=None)
c = conn.cursor()

## 테이블 생성

c.execute("DROP TABLE KOSPI200")
c.execute("CREATE TABLE IF NOT EXISTS KOSPI200 (tickers text PRIMARY KEY, full_name text,"
          "market_cap integer, Lastprice integer)")
c.execute("INSERT INTO KOSPI200 VALUES ('005930 KS Equity', '삼성전자',354605083,59500)")

c.execute("INSERT INTO KOSPI200(tickers, full_name, market_cap, Lastprice) VALUES(?,?,?,?) ",
          ('000660 KS Equity', 'sk하이닉스', 69378625, 95500))

test_tuple = (
    ('373220 KS Equity', 'LG에너지솔루션', 96057000, 410500),
    ('207940 KS Equity', '삼성바이오로직스', 58006810, 815000))

c.executemany("INSERT INTO KOSPI200(tickers, full_name, market_cap, LastPrice) VALUES(?,?,?,?)", test_tuple)

c.execute("DELETE FROM KOSPI200 WHERE tickers='005930 KS Equity'")


