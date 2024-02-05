import xlwings

def excel_editing():
    wb=xlwings.Book(r"/Users/hyelim/xlwings.xlsm").caller()
    sheet=wb.sheets[0]
    sheet["A1"].value="커리어하이"
    sheet["A2"].value="안녕하세요"

def breaking_news():
    wb=xlwings.Book(r"/Users/hyelim/xlwings.xlsm").caller()
    sheet=wb.sheets[0]
    import requests
    from bs4 import BeautifulSoup
    webpage=requests.get("https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258")
    soup=BeautifulSoup(webpage.content,"html.parser")
    for index, i in enumerate(soup.dd.find_all('a')):
        sheet["B"+str(index+1)].value=i.text


excel_editing()
breaking_news()
