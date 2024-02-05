import pandas as pd
import datetime
## 1.Pykrx 모듈을 활용하여 최근일주일간 kospi전종목의 종가 dataframe 과 거래대금 dataframe 만들기

from pykrx import stock
today = datetime.datetime.today().date()
startDay = today - datetime.timedelta(days=7)
startDay_str = startDay.strftime("%Y%m%d")
today_str = today.strftime("%Y%m%d")


kospi_tickers = stock.get_market_ticker_list(today_str, market="KOSPI")

closing_price = pd.DataFrame(index=pd.date_range(startDay_str, today_str),columns=kospi_tickers)
volumn = pd.DataFrame(index=pd.date_range(startDay_str, today_str),columns=kospi_tickers)

print(kospi_tickers)
for idx, ticker in enumerate(kospi_tickers):
    temp = stock.get_market_ohlcv(startDay_str, today_str, ticker) ## 시가, 저가, 종가, 거래량, 거래대금, 등락률 등 가져옴
    print(type(temp["종가"]))
    print(type(closing_price[ticker]))
    closing_price[ticker] = temp["종가"]
    volumn[ticker] = temp["거래량"]
print(closing_price)
print(volumn)

closing_price=closing_price.dropna(how='all', axis=0)
volumn=volumn.dropna(how='all', axis=0)

closing_price.to_excel(excel_writer="./closing_price.xlsx")
volumn.to_excel(excel_writer="./volumn.xlsx")


