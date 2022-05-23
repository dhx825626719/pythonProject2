import time
import random
import requests

url1 = "http://api.pupu.chat/v2/gift/room/1001/send"
url2 = "http://api.pupu.chat/v2/game/ferrule/play"

payload1='uIds=103&giftKey=100&giftNum=1&type=2'
payload2='roomId=1004&gameId=2&rewardId='
headers1 = {
  'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20ubWFpdGFuZy5oaWxhIiwiaWF0IjoxNjUwODU2ODUyLCJleHAiOjE2NTExMTYwNjIsIm5iZiI6MTY1MDg1Njg1MiwianRpIjoiMDc2YzQyYzQ0ZDZiOTVkMzExYzkwY2U5MDVmYTA0YTEiLCJzdWIiOjEzNCwicHJ2IjoidXNlciJ9.0nUU5GRVLhkFTJkhHZ7i3quWsXaKWEIGg9mAEYwuAgQ',
  'channel': 'BETA',
  'appType': 'Android',
  'language': 'zh-TW',
  'Host': 'api.pupu.chat',
  'User-Agent': 'okhttp/4.9.0',
  'Content-Type': 'application/x-www-form-urlencoded'
}
headers2 = {
  'Host': 'api.pupu.chat',
  'Accept': 'application/json, text/plain, */*',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2102J2SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 AgentWeb/v1.5.2  UCBrowser/11.6.4.950',
  'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20ubWFpdGFuZy5oaWxhIiwiaWF0IjoxNjUwODc2Njg1LCJleHAiOjE2NTExMzU4OTUsIm5iZiI6MTY1MDg3NjY4NSwianRpIjoiNmU0ZTIzODdhY2Y0NGZiM2I1OWMyNzAwNjhkZTQ5MWQiLCJzdWIiOjE0MywicHJ2IjoidXNlciJ9.ssNULWvIqyUpP9tlSDS6iRop8Kfa3AV6A1FuhNntpXM',
  'Origin': 'http://front.pupu.chat',
  'X-Requested-With': 'com.maitang.hila',
  'Referer': 'http://front.pupu.chat/',
  'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'Content-Type': 'application/x-www-form-urlencoded'
}

a=1
while True:
  b=random.randint(1,15)
  d=str(random.randint(1,20))
  pay =payload2+d
  print(pay)
  time.sleep(b)
  response1 = requests.request("POST", url1, headers=headers1, data=payload1)
  response2 = requests.request("POST", url2, headers=headers2, data=pay)
  a=a+1
  print(response1.text)
  print(response2.text)
  print(a)

