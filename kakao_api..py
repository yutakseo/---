import requests
import json
from crawler import *

date = crawler_machine(0)

with open("kakao_code.json", "r") as fp:
    tokens = json.load(fp)    
print(tokens["access_token"])

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + "-RI9gj07Kx5z2_qexnyMvBHPlfkQeYCSCDORF6LmCisMpgAAAYrlKItD"
}
data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "%s" ,
                                     "link" : {}
    })
}
response = requests.post(url, headers=headers, data=data)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))