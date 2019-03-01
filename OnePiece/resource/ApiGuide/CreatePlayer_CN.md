## 创建新玩家

### URL
http://test.magcore.clawit.com/api/player

### Method
POST

### Header
Content-Type: application/json

### Body
```json
{
	"Name": "Cola",
	"Color": 0
}
```

Name: 欲创建玩家的昵称
Color: 欲选择的颜色(0~9可选)

### 返回结果
成功 Status Code: 200
失败 Status Code: 409

Content: 
```json
{
    "Id": "784f7580cfba4344b039edecb8876dda",
    "Name": "Cola",
    "Token": "1e2e222bbca6493f9d5d740e9b70929b",
    "Energy": 0,
    "Color": 0,
    "State": 0,
    "Index": 2,
    "Bases": []
}
```

Id: 新创建的玩家Id

Name: 新创建的玩家昵称

Token: 新创建的玩家安全令牌(暂保留)

Energy: 新创建的玩家能量(暂保留)

Color: 新创建的玩家颜色

State: 新创建的玩家状态

Index: 新创建的玩家标识号

Bases: 新创建的玩家基地**数组**(暂保留)

### 示例
#### Python
```python
import requests

url = "http://test.magcore.clawit.com/api/player"

payload = "{\"Name\":\"Cola\", \"Color\":0}"
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
```

#### JavaScript
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://test.magcore.clawit.com/api/player",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
  },
  "processData": false,
  "data": "{\"Name\":\"Cola\", \"Color\":0}"
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```