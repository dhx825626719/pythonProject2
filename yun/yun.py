import requests
import requests
import time
import hashlib
import json
import base64
APP_KEY = '8e1dba7a8dc34e72733516fe20f319f9'
APP_SECRET = '90db4df262c2'
#先获取当前时间戳，单位毫秒
curTime =str(time.time())
#设置过期时间，单位秒，如600
ttl = str(600)
accid=str(7417521)
#生成signature，将appkey、accid、curTime、ttl、appsecret五个字段拼成一个字符串，进行sha1编码
signature = hashlib.sha1((APP_KEY + accid + curTime + ttl + APP_SECRET).encode('utf8')).hexdigest()
#组装成json
json = json.dumps([{"signature": signature, "curTime":curTime, "ttl": 600}])
#将json转成字符串后进行base64编码，生成最终的token
token=base64.b64encode(bytes(json, encoding = "utf8"))
print(token)
CheckSum=hashlib.sha1((str(APP_SECRET) + '4tgggergigwow323t23t' + str(curTime)).encode('utf8')).hexdigest()

url = "https://api.netease.im/nimserver/history/querySessionMsg.action"

payload='begintime=0&endtime=9443599639999&from=7417521&to=7418385&limit=50'
headers = {
  'AppKey': str(token),
  'Nonce': '4tgggergigwow323t23t',
  'CurTime': curTime,
  'CheckSum': CheckSum,
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
