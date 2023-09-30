import bs4 
import requests
import re


def crawler_machine(numb):
    url = 'https://exam.toeic.co.kr/receipt/examSchList.php'
    contents = []

    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = bs4.BeautifulSoup(html, 'html.parser')
        print("접속성공")
        
        for i in range(10):
            temp = soup.select("div.table_data table tbody tr:nth-child(%d) td:nth-child(2)" %i)
            if temp:
                contents.append(temp[0].get_text())
    else : 
        print(response.status_code)
    for i in range(len(contents)):
        contents[i] = re.sub("\n", "", contents[i]).strip().replace("    ", "")
    
    return contents[numb]


print(crawler_machine(0))