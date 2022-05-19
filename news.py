from wsgiref import headers
import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0(window NT 6.3; Win64; x64) Applewebkit/537.36 (KHTML,like Gecko) Chrome/63.0'}

# 검색할 키워드 입력
search = input("검색할 키워드를 입력해주세요: ")
# 검색할 페이지 입력
page = int(input("원하는 크를링할 페이지(숫자)를 입력해주세요"))

page_num = 1
if page:
    page_num = (page-1)*10+1
    
url = "https://search.naver.com/search.naver?where=newe&sm=tab_pge&query=" + search +"&start=" + str(page_num)
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,"html.parse")

articles = soup.select("div.group_news > ul.list_news > li div.news_area >a")
# print(articles)

print("네이버에 '",search,"' 를 검색했을 때의 뉴스 기사 ", end="\n")
print(page,"페이지의",end=" ")
print(len(articles),"개의 기사가 검색됌",end= "\n\n")

article_file = open("article.txt","a",encoding="utf-8")

i = 1
for article in articles:
    article_file.write(str(i)+"번째 기사"+article.get_text()+"\n")
    print(str(i)+"번째 기사 : " + article.get_text(),"\n")
    i += 1