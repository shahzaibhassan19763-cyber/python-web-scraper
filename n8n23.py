import requests
from bs4 import BeautifulSoup
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

data=[]
for page in range(1,5):
    url=f"http://books.toscrape.com/catalogue/page-{page}.html"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")

    books=soup.find_all("article",class_="product_pod")
    for book in books:
        book_title=book.find('h3').get_text()
        book_price=book.find(class_="price_color").get_text()
        data.append({"title":book_title,"price":book_price})
try:
    url2 = "https://pointer-animating-garnet.ngrok-free.dev/webhook-test/b35088b1-3c0e-4273-9595-dece1a11f8b1"
    payload = requests.post(url2, json=data)
    
    if payload.status_code == 200:
        print("Success:", payload.json())
    else:
        print("Failed with status code:", payload.status_code)

except Exception as e:
    print("An error occurred:", e)