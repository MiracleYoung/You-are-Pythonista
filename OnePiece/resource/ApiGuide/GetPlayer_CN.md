## 获取玩家信息

### URL
http://test.magcore.clawit.com/api/player/{PlayerId}

{PlayerId}: 欲获取信息的玩家Id

### Method
GET

### 返回结果
成功 Status Code: 200

失败 Status Code: 404

Content: 
```json
{
    "Id": "784f7580cfba4344b039edecb8876dda",
    "Name": "Cola",
    "Token": "1e2e222bbca6493f9d5d740e9b70929b",
    "Energy": 0,
    "Color": 0,
    "State": 1,
    "Index": 2,
    "Bases": [
        "3,7"
    ]
}
```

Id: 玩家Id

Name: 玩家昵称

Token: 玩家安全令牌(暂保留)

Energy: 玩家能量(暂保留)

Color: 玩家颜色

State: 玩家状态

Index: 玩家标识号

Bases:玩家基地坐标**数组**

### 示例
#### Python
```python
import requests

url = "http://test.magcore.clawit.com/api/player/784f7580cfba4344b039edecb8876dda"

headers = {
    'Cache-Control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
```

#### JavaScript
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://test.magcore.clawit.com/api/player/784f7580cfba4344b039edecb8876dda",
  "method": "GET",
  "headers": {
    "Cache-Control": "no-cache"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```