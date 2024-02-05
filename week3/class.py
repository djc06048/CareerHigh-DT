# 파이썬 패키지 활용
from pykrx import stock

tickers = stock.get_market_ticker_list('2000-01-01', market='KOSPI')
print(stock.get_market_ticker_name(tickers[0]))

df = stock.get_market_ohlcv("20220101", "20220628", "005930")
print(df)

df = stock.get_market_ohlcv("20220122", market="KOSPI")
df=stock.get_market_price_change("20180301","20180320")
print(df)

df=stock.get_market_fundamental("20210108")
df=stock.get_market_cap("20220628")

# DART 활용 - 금융감독원 공시시스템

KEY="a6edc2fba9087b997c86e48255fb8113e146ee8d"
from xml.etree.ElementTree import parse
import pandas as pd
xmlTree=parse(r"./CORPCODE.xml")
root=xmlTree.getroot()
temp_list=root.findall('list')
print(len(temp_list[0].findtext('corp_code')))

list_for_df=[]

for i in range(0,len(temp_list)):
    temp=temp_list[i]
    list_for_df.append([temp.findtext('corp_code'),temp.findtext('corp_name'),temp.findtext('stock_code'),temp.findtext('modify_date')])
corp_code_df=pd.DataFrame(list_for_df,columns=['corp_code','corp_name',
                                               'stock_code','modify_date'])
corp_code_df.to_excel(r"./CORPCODE.xlsx")

from bs4 import BeautifulSoup
import requests

def get_search(bgn_de,end_de,page_no,page_count,pblntf_ty="B"):
    key="a6edc2fba9087b997c86e48255fb8113e146ee8d"
    url="https://opendart.fss.or.kr/api/list.xml"
    params={'crtfc_key':key,'bgn_de':bgn_de,'end_de':end_de,\
            'page_no':page_no,'page_count':page_count,'pblntf_ty':pblntf_ty}
    response=requests.get(url,params=params).content.decode('UTF-8')
    html=BeautifulSoup(response,'html.parser')
    res=html.findAll('list')
    print(res)
    return res

from datetime import datetime as dt
today=dt.today()
today_str=today.strftime("%Y%m%d")
print(today_str)
today='20220704'

result=get_search(today_str,today_str,1,100)
list_for_df=[]
for i in result:
    print(i.corp_code.text,i.flr_nm.text,i.report_nm.text,i.rcept_no.text)
    list_for_df.append([i.corp_code.text,i.flr_nm.text,i.report_nm.text,\
                        "https://dart.fss.or.kr/dsaf001/main.do?rcpNo="+i.rcept_no.text])

    print(list_for_df)

rcept_df=pd.DataFrame(list_for_df,columns=['회사코드','회사명','공시내용','공시링크'])
rcept_df.to_excel(r'./공시내용정리.xlsx')
