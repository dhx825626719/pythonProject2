import time
import random
import requests

url1 = "http://api.pupu.chat/v2/gift/room/1001/send"
url2 = "http://api.pupu.chat/v2/game/ferrule/play"

payload1='uIds=126&giftKey=100&giftNum=1&type=2'
payload2='roomId=1004&gameId=2&rewardId='
headers1 = {
  'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20ubWFpdGFuZy5oaWxhIiwiaWF0IjoxNjUxNTcwMTUwLCJleHAiOjE2NTE4MjkzNjAsIm5iZiI6MTY1MTU3MDE1MCwianRpIjoiNjA3OTEyZTA4MjdhYTFhOTcwMWQ1ODI4YzI4ODI3ZTciLCJzdWIiOjEyNiwicHJ2IjoidXNlciJ9.k3Z36slZ1Tzy1HnH91w5uTVbV3yh5MJeCayGT1PQmjY',
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
  'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20ubWFpdGFuZy5oaWxhIiwiaWF0IjoxNjUxNTcwMTUwLCJleHAiOjE2NTE4MjkzNjAsIm5iZiI6MTY1MTU3MDE1MCwianRpIjoiNjA3OTEyZTA4MjdhYTFhOTcwMWQ1ODI4YzI4ODI3ZTciLCJzdWIiOjEyNiwicHJ2IjoidXNlciJ9.k3Z36slZ1Tzy1HnH91w5uTVbV3yh5MJeCayGT1PQmjY',
  'Origin': 'http://front.pupu.chat',
  'X-Requested-With': 'com.maitang.hila',
  'Referer': 'http://front.pupu.chat/',
  'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'Content-Type': 'application/x-www-form-urlencoded'
}

a=1
while True:
  b=random.randint(30,100)
  d=str(random.randint(1,20))
  pay =payload2+d
  print(b)
  print(pay)
 # response1 = requests.request("POST", url1, headers=headers1, data=payload1)
  response2 = requests.request("POST", url2, headers=headers2, data=pay)
  a=a+1
 # print(response1.text)
  print(response2.text)
  print(a)
  time.sleep(b)

