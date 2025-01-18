# API
import requests

## ISS 위치 알려주는 API
res = requests.get(url = "http://api.open-notify.org/iss-now.json")
print(res) #<Response [200]>

res.raise_for_status() #HTTP 에러 raise

payload = res.json()
print(payload) #json으로 실행


