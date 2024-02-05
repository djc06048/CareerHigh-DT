import datetime

import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
from pykrx import stock


def get_kospi_list_today():
    today = datetime.datetime.today()
    today_str = today.strftime("%Y%m%d")

    kospi_200_list = stock.get_market_ticker_list(date=today_str, market="KOSPI")
    return kospi_200_list


def datelist_oneyear():
    today = datetime.datetime.today()
    today_str = today.strftime("%Y%m%d")
    startdate = today - relativedelta(years=1)
    startdate_str = startdate.strftime("%Y%m%d")

    date_range = pd.date_range(start=startdate_str, end=today_str)
    datelist = []
    for date in date_range:
        datelist.append(date.strftime("%Y%m%d"))
    return datelist


def get_historical_data(datelist):
    res = pd.DataFrame()
    for d in datelist:
        df = stock.get_market_ohlcv(d, market="KOSPI")
        df = df.assign(일자=d)
        res = pd.concat([res, df], axis=0)
        print(d)

    res = res.assign(티커=res.index)
    print(res)
    res = (res.replace(0, np.nan)).dropna(subset=["시가", "고가", "저가", "종가", "거래량", "거래대금", "등락률"], how="all", axis=0)

    return res


datelist = datelist_oneyear()


# res = get_historical_data(datelist)


def get_someday_data():
    import sqlite3
    from pathlib import Path
    path = Path.cwd()
    dbpath = path / "finalProject.db"
    conn = sqlite3.connect(dbpath, isolation_level=None)
    c = conn.cursor()
    today_str = datetime.datetime.today().strftime("%Y%m%d")

    c.execute("SELECT * FROM KOSPI_LASTPRICE kl where kl.DATE=?", (today_str,))
    existing_record = c.fetchone()
    if existing_record is None:
        s = stock.get_market_ohlcv(date=today_str, market="KOSPI")
        print(s)

        input_data1 = []
        input_data2 = []
        for i in range(len(s.index)):
            temp1 = [s.index[i], today_str, s.iloc[i].loc["종가"]]

            temp2 = [s.index[i], today_str, s.iloc[i].loc["거래대금"]]

            temp1[-1] = int(temp1[-1])
            temp2[-1] = int(temp2[-1])
            input_data1.append(tuple(temp1))
            input_data2.append(tuple(temp2))

        input_data1 = tuple(input_data1)
        input_data2 = tuple(input_data2)

        c.executemany("INSERT INTO KOSPI_LASTPRICE(TICKER, DATE, LASTPRICE) VALUES(?,?,?)", input_data1)
        c.executemany("INSERT INTO KOSPI_TA (TICKER, DATE, TRADINGAMOUNT) VALUES(?,?,?)", input_data2)


get_someday_data()


def db_save_price_one_year(res):
    import sqlite3
    from pathlib import Path
    path = Path.cwd()
    dbpath = path / "finalProject.db"
    conn = sqlite3.connect(dbpath, isolation_level=None)
    c = conn.cursor()
    c.execute("CREATE TABLE KOSPI_LASTPRICE \
    (TICKER text, DATE text, LASTPRICE integer )")
    c.execute("CREATE TABLE KOSPI_TA \
    (TICKER text, DATE text, TRADINGAMOUNT integer )")
    input_data1, input_data2 = [], []
    res = res.fillna(0)
    for i in range(len(res.index)):
        temp1 = res.iloc[i, [-1, -2, -6]].tolist()
        temp2 = res.iloc[i, [-1, -2, -4]].tolist()
        temp1[-1] = int(temp1[-1])
        temp2[-1] = int(temp2[-1])
        input_data1.append(tuple(temp1))
        input_data2.append(tuple(temp2))
        print(res.iloc[i].loc["일자"])
    input_data1 = tuple(input_data1)
    input_data2 = tuple(input_data2)
    c.executemany("INSERT INTO KOSPI_LASTPRICE(TICKER, DATE, LASTPRICE) VALUES(?,?,?)", input_data1)
    c.executemany("INSERT INTO KOSPI_TA (TICKER, DATE, TRADINGAMOUNT) VALUES(?,?,?)", input_data2)


# db_save_price_one_year(res)

def db_parsing_for_1year():
    import sqlite3
    from pathlib import Path
    path = Path.cwd()
    dbpath = path / "finalProject.db"
    conn = sqlite3.connect(dbpath, isolation_level=None)
    c = conn.cursor()
    c.execute("SELECT * FROM KOSPI_LASTPRICE")
    arr = c.fetchall()

    df = pd.DataFrame(arr, columns=['티커', '날짜', '종가'])
    result_df = df.pivot(index='날짜', columns='티커', values='종가')
    print(result_df)

    # 수익률과 공분산 행렬
    price_difference = result_df.diff()
    price_shift = result_df.shift(1)
    return_frame = price_difference / price_shift
    return_frame = return_frame.dropna(axis=1)

    cov=return_frame.cov().values
    return_val=return_frame.mean().values

    n_stocks=len(return_val)
    w_init=np.ones(n_stocks)/n_stocks
    from scipy import optimize
    constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})

    bounds = tuple((0, 1) for _ in range(n_stocks))

    res = optimize.minimize(Volatility_Of_Port, w_init, args=(cov,),
                            method='SLSQP', bounds=bounds, constraints=constraints)

    optimized_weights = res.x
    print("Optimal Weights:", optimized_weights)

    Volatility_Of_Port(optimized_weights,cov)
    Return_Of_Port(optimized_weights,return_val)
    return optimized_weights



def Volatility_Of_Port(w,cov):
    return np.dot(np.dot(w,cov),w)
def Return_Of_Port(w,ret):
    w = np.array(w)/sum(w)
    return np.dot(w,np.array(ret))

w= db_parsing_for_1year()
