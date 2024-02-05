
import pandas as pd
import datetime
from pykrx import stock
import requests
from bs4 import BeautifulSoup
# 자신의 path 를 입력해주세요
path=r"/Users/hyelim/study/2024-CareerHigh-DT/study/week3"

def dart():
    today = datetime.datetime.today()
    today_str = datetime.datetime.strftime(today, '%Y%m%d')
    today_table_ = stock.get_market_ohlcv(today_str, market="KOSPI")
    today_table_ = today_table_.sort_values(by=['거래대금'], ascending=False)
    tickers_best20 = today_table_.index[:20]

    from xml.etree.ElementTree import parse
    xmlTree = parse(path+ r"/CORPCODE.xml")
    root = xmlTree.getroot()
    temp_list = root.findall('list')
    list_for_df = []
    for i in range(0, len(temp_list)):
        temp = temp_list[i]
        list_for_df.append([temp.findtext('corp_code'), temp.findtext('corp_name') \
                               , temp.findtext('stock_code'), temp.findtext('modify_date')])
    corp_code_df = pd.DataFrame(list_for_df, columns=['corp_code', 'corp_name', 'stock_code', 'modify_date'])

    # 최종 티커,종목명,corpcode를 박아넣는다. #dataframe.isin 검색 후 true인부분만 추출하게 하는 방법
    final_list = corp_code_df[corp_code_df['stock_code'].isin(tickers_best20)]


    key = "a6edc2fba9087b997c86e48255fb8113e146ee8d"
    url = "https://opendart.fss.or.kr/api/list.xml"

    result = pd.DataFrame(columns=['종목명', '거래대금', '공시제목', '공시링크'])
    cnt = 1  # 공시수 담을것
    for i in final_list.index: # 20 개
        params = {'crtfc_key': key, 'bgn_de': today_str, 'end_de': today_str, \
                  'page_no': 1, 'page_count': 100, 'corp_code': final_list.loc[i, 'corp_code']}
        # url에 요청인자 추가해서 컨텐츠 내려받기 (UTF-8형식 변환해서)
        response = requests.get(url, params=params).content.decode('UTF-8')
        # 받은 컨텐츠를 html으로 parsing
        html = BeautifulSoup(response, 'html.parser')
        # html 파일에서 list 태그 가져오기
        res = html.findAll('list')

        for j in res:
            result.loc[cnt, :] = [final_list.loc[i, 'corp_name'],
                                  today_table_.loc[final_list.loc[i, 'stock_code']]['거래대금'], \
                                  j.report_nm.text, "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=" + j.rcept_no.text]
            cnt += 1

    print(result)
    return result
result1= dart()
print(result1)

def news():
    today = datetime.datetime.today()
    today_str = datetime.datetime.strftime(today, '%Y%m%d')
    today_table_ = stock.get_market_ohlcv(today_str, market="KOSPI")
    today_table_ = today_table_.sort_values(by=['거래대금'], ascending=False)
    tickers_best20 = today_table_.index[:20]

    from xml.etree.ElementTree import parse
    xmlTree = parse(path+ r"/CORPCODE.xml")

    root = xmlTree.getroot()
    temp_list = root.findall('list')
    list_for_df = []
    for i in range(0, len(temp_list)):
        temp = temp_list[i]
        list_for_df.append([temp.findtext('corp_code'), temp.findtext('corp_name') \
                               , temp.findtext('stock_code'), temp.findtext('modify_date')])
    corp_code_df = pd.DataFrame(list_for_df, columns=['corp_code', 'corp_name', 'stock_code', 'modify_date'])

    # 최종 티커,종목명,corpcode를 박아넣는다.
    final_list = corp_code_df[corp_code_df['stock_code'].isin(tickers_best20)]

    import urllib
    import requests
    from bs4 import BeautifulSoup

    today_str2 = datetime.datetime.strftime(today, '%Y-%m-%d')
    result = pd.DataFrame(columns=['종목명', '거래대금', '기사제목', '기사링크'])
    cnt = 1  # 기사갯수 담기
    for q in final_list['corp_name']:
        q_enc = urllib.parse.quote_plus(q, encoding='euc-kr')
        webpage = requests.get("https://finance.naver.com/news/news_search.naver?q=" + q_enc \
                               + '&sm=title.basic&pd=1&stDateStart=' + today_str2 + '&stDateEnd=' + today_str2)
        soup = BeautifulSoup(webpage.content, "html.parser")
        # elem_news = soup.select_one('div.newsSchResult dl.newsList')
        # elem_news()
        elems_sub = soup.select('.articleSubject ')

        for i in elems_sub:
            기사제목 = i.text.strip()
            기사article_id = i.a.get('href')
            티커명 = final_list[final_list['corp_name'] == q].iloc[0, 2]
            result.loc[cnt, :] = [q, today_table_.loc[티커명, '거래대금'], \
                                  기사제목, "https://finance.naver.com" + 기사article_id]
            cnt += 1
    print(result)
    return result

result2= news()
def ret():
    today = datetime.datetime.today()
    yesterday=today-datetime.timedelta(days=1)

    today_str = datetime.datetime.strftime(today, '%Y%m%d')
    yesterday_str=datetime.datetime.strftime(yesterday,"%Y%m%d")

    today_table_ = stock.get_market_ohlcv(today_str, market="KOSPI")
    yesterday_table_=stock.get_market_ohlcv(yesterday_str,market="KOSPI")

    today_table_ = today_table_.sort_values(by=['거래대금'], ascending=False)
    tickers_best20 = today_table_.index[:20]
    yesterday_table_=yesterday_table_[yesterday_table_.index.isin(tickers_best20)]
    yesterday_lastprice=[]
    for ticker in tickers_best20:
        yesterday_table_ = yesterday_table_.sort_values(by=['거래대금'], ascending=False)
        yesterday_lastprice.append(yesterday_table_.loc[ticker].loc["종가"])

    print(yesterday_lastprice)
    result=today_table_[:20]
    data=pd.DataFrame(index=tickers_best20)
    lastpricelist=[]
    stocknamelist=[]
    indexlist=[]
    for idx,ticker in enumerate(tickers_best20):
        name= stock.get_market_ticker_name(ticker)
        stocknamelist.append(name)
        lastpricelist.append(result.loc[ticker].loc['종가'])
        indexlist.append(idx+1)
    data=data.assign(종목명=stocknamelist)
    data=data.assign(종가=lastpricelist)
    data=data.assign(전날=yesterday_lastprice)
    data.index=indexlist
    price_diff=data["종가"]-data["전날"]
    ret=price_diff/data["전날"]
    data["수익률"]=ret
    data=data.drop(columns="종가")
    data=data.drop(columns="전날")

    print(data)

    return data

result3=ret()


def final():
    import pandas as pd
    result1=dart()
    result2=news()
    result3=ret()
    with pd.ExcelWriter(r"/Users/hyelim/study/2024-CareerHigh-DT/study/week4"+r"/4week_final.xlsx") as writer:
        result1.to_excel(writer,sheet_name="공시자료",index=False)
        result2.to_excel(writer,sheet_name="뉴스",index=False)
        result3.to_excel(writer,sheet_name="수익률",index=False)
    return 0


import datetime


def kospidata_to_DB(date=datetime.datetime.today()):
    import sqlite3
    from pykrx import stock
    from pathlib import Path
    path = Path.cwd()
    dbpath = path.parent.parent / "test.db"
    conn = sqlite3.connect(dbpath, isolation_level=None)
    c = conn.cursor()
    today_str = datetime.datetime.strftime(date, "%Y%m%d")

    today_table = stock.get_market_ohlcv(today_str, market="KOSPI")
    today_table = today_table.assign(일자=today_str, 티커=today_table.index)
    input_data1_, input_data2_ = [], []
    for i in range(len(today_table.index)):
        temp1_ = today_table.iloc[i, [-1, -2, -6]].tolist()
        temp2_ = today_table.iloc[i, [-1, -2, -4]].tolist()
        temp1_[-1] = int(temp1_[-1])
        temp2_[-1] = int(temp2_[-1])
        input_data1_.append(tuple(temp1_))
        input_data2_.append(tuple(temp2_))
    input_data1_ = tuple(input_data1_)
    input_data2_ = tuple(input_data2_)
    c.executemany("INSERT INTO KOSPI_LASTPRICE(TICKER, DATE, LASTPRICE) VALUES(?,?,?)", input_data1_)
    c.executemany("INSERT INTO KOSPI_TA (TICKER, DATE, TRADINGAMOUNT) VALUES(?,?,?)", input_data2_)
    print("DB insert 완료")
    c.close()
    conn.close()
    return 0
final()
