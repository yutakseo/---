import bs4 
import requests
import re

url = 'https://exam.toeic.co.kr/receipt/examSchList.php'
contents = []

response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    print("접속성공")
    
    # 유효한 CSS 선택자를 사용하여 원하는 요소를 찾습니다.
    for i in range(10):
        temp = soup.select("div.table_data table tbody tr:nth-child(%d) td:nth-child(2)" %i)
        if temp:
            # 내용이 비어 있지 않은지 확인합니다.
            contents.append(temp[0].get_text())
else : 
    print(response.status_code)
    

for i in range(len(contents)):
    contents[i] = re.sub("\n", "", contents[i]).strip().replace("    ", "")
    
print(contents)
