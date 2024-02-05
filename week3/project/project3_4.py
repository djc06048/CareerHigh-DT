import pandas as pd
from pykrx import stock
from datetime import datetime
df=stock.get_market_ohlcv_by_ticker(datetime.today().date().strftime("%Y%m%d"),market="KOSPI")
top20_stock=df.sort_values(by="거래대금",ascending=False).head(20)



import urllib
import requests
from bs4 import BeautifulSoup

def 상위20개종목뉴스가져오기():
    result = pd.DataFrame(columns=['종목명', '거래대금', '기사제목', '기사링크'])
    cnt=1
    for ticker in top20_stock.index:
        거래대금=top20_stock.loc[ticker]["거래대금"]
        q= stock.get_market_ticker_name(ticker)
        q_enc = urllib.parse.quote_plus(q, encoding='euc-kr')
        today_str=datetime.today().strftime("%Y-%m-%d")
        url="https://finance.naver.com/news/news_search.naver?q="+q_enc+'&sm=title.basic&pd=1&stDateStart=' + today_str + '&stDateEnd=' + today_str
        webpage = requests.get(url)

        soup = BeautifulSoup(webpage.content, "html.parser")

        elems_sub = soup.select('.articleSubject ')

        for i in elems_sub:
            기사제목 = i.text.strip()
            기사article_id = i.a.get('href')
            티커명 = ticker
            result.loc[cnt,:]=[q,거래대금,기사제목, "https://finance.naver.com" + 기사article_id]
            cnt=cnt+1

    print(result)
    return result

뉴스=상위20개종목뉴스가져오기()
