import requests
import json

url = "http://192.168.10.125:8081/address"

payload = json.dumps({
  "entity_no": 0,
  "entrust_id": "10101",
  "task_id": "10101",
  "begin_time": "2024-09-14 11:14:00",
  "returnUrl": "http://192.168.3.233:8000/api/receive",
  "customer_info": [
    {
      "customer_id": "101",
      "homeAddress": "福建省厦门市思明区仙阁里114号304室福建省厦门市思明区仙阁里114号304室",
      "beginTime": "2024-09-14 11:14:00",
      "liveAddress": "福建省厦门市思明区仙阁里114号304室福建省厦门市思明区仙阁里114号304室",
      "user_identification": "421122200010104321"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


