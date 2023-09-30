import requests
import json

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "refresh_token",
    "client_id": "9ccefd64c636f1689a2c14ec08899cd3",
    "refresh_token": "_aKSrtgY1RM1lnSdoTXA9HrmFouX-fdggFR9vKLHCisNIAAAAYrlJxqw"
}
response = requests.post(url, data=data)
tokens = response.json()
# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)