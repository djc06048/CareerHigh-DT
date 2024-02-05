from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt
import pandas as pd
from pykrx import stock

today = dt.today()
today_str = today.strftime("%Y%m%d")
today_table_ = stock.get_market_ohlcv(today_str, market= "KOSPI")
today_table_=today_table_.sort_values(by="거래대금",ascending=False)
tickers_best20=today_table_.index[:20]

KEY = "a6edc2fba9087b997c86e48255fb8113e146ee8d"


def get_search(bgn_de, end_de, page_no, page_count,corp_code):
    url = "https://opendart.fss.or.kr/api/list.xml"
    params = {'crtfc_key': KEY, 'bgn_de': bgn_de, 'end_de': end_de, \
              'page_no': page_no, 'page_count': page_count, 'corp_code':corp_code }
    response = requests.get(url, params=params).content.decode('UTF-8')
    html = BeautifulSoup(response, 'html.parser')
    res = html.findAll('list')
    print(res)
    return res


stock_data = stock.get_market_ohlcv_by_ticker(today, market="KOSPI")
top20_stock = stock_data.sort_values(by="거래대금", ascending=False).head(20)

corp_code = pd.ExcelFile(r"../CORPCODE.xlsx").parse(0)
print(corp_code)

list_for_df = []

for index, row in top20_stock.iterrows():
    print(index, row)
    종목명 = stock.get_market_ticker_name(index)
    corp_info = corp_code[corp_code['corp_name'] == 종목명]
    print(corp_info)

    # if not corp_info.empty:
    result = get_search(today_str, today_str, 1, 100,index)
    for i in result:
        거래대금=row["거래대금"]
        list_for_df.append([i.flr_nm.text, 거래대금, i.report_nm.text, \
                            "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=" + i.rcept_no.text])

    print(list_for_df)

rcept_df = pd.DataFrame(list_for_df, columns=['회사명','거래대금', '공시내용', '공시링크'])
print(rcept_df)

## corp_code 모든 회사의 코드(상장여부 관계 없음)
## 최종 티커, 종목명, corpcode 를 박아넣는다.
## final_list=corp_code_df[corp_code_df['stock_code'].isin(tickers_best20)]
## 한종목당 공시 100개까지 - page_no=1 page_count=100

# https://finance.naver.com/news/news_search.naver 이용하기
# soup.select

# 장이 끝난 후 리서치 자료 전달하는 서비스 작업 - 이벤트 발생(오늘의 공시(팩트), 뉴스기사) -  금융사 크롤링 대표적인 프로젝트 - 주니어 담당
1
