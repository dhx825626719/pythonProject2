import time
import random
import requests

url1 = "http://api.pupu.chat/v2/gift/room/1001/send"

payload1 = 'uIds=103&giftKey=500&giftNum=1&type=2'
headers1 = {
  'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20ubWFpdGFuZy5oaWxhIiwiaWF0IjoxNjUwODU2ODUyLCJleHAiOjE2NTExMTYwNjIsIm5iZiI6MTY1MDg1Njg1MiwianRpIjoiMDc2YzQyYzQ0ZDZiOTVkMzExYzkwY2U5MDVmYTA0YTEiLCJzdWIiOjEzNCwicHJ2IjoidXNlciJ9.0nUU5GRVLhkFTJkhHZ7i3quWsXaKWEIGg9mAEYwuAgQ',
  'channel': 'BETA',
  'appType': 'Android',
  'language': 'zh-TW',
  'Host': 'api.pupu.chat',
  'User-Agent': 'okhttp/4.9.0',
  'Content-Type': 'application/x-www-form-urlencoded'
}

a=1
while True:
  b=random.randint(1,15)
  d=str(random.randint(1,20))
  time.sleep(b)
  response1 = requests.request("POST", url1, headers=headers1, data=payload1)

  a=a+1
  print(response1.text)
  print(a)



