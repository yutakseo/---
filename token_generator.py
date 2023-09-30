import requests
import json

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "9ccefd64c636f1689a2c14ec08899cd3",
    "redirect_url" : "https://localhost:3000",
    "code" : "6vWisoqrSiLpEH78EPoOLnn9UKkx4OF7B5ULZyjGsO_BenK21i-q4mQzzHsafQLQWmrO-go9c5oAAAGK5SFR2w"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)
