## 攻击单元

### URL
http://test.magcore.clawit.com/api/cell/

### Method
PUT

### Header
Content-Type: application/json

### Body
```json
{
	"Game": "382bb353448f4c4d9637263518c085b9",
	"Player": "48d19c8b4419409a9a63dfd1c8152db2",
	"X": 2,
	"Y": 4
}
```

Game: 欲攻击单元的所属游戏Id

Player: 玩家自己的PlayerId

X: 欲攻击单元的x坐标

Y: 欲攻击单元的y坐标

### 返回结果
成功 Status Code: 200

失败 Status Code: 404

### 示例
#### Python
```python
import requests

url = "http://test.magcore.clawit.com/api/cell/"

payload = "{\"Game\":\"382bb353448f4c4d9637263518c085b9\", \"Player\":\"48d19c8b4419409a9a63dfd1c8152db2\", \"X\":2, \"Y\":4}"
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)
```

#### JavaScript
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://test.magcore.clawit.com/api/cell/",
  "method": "PUT",
  "headers": {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
  },
  "processData": false,
  "data": "{\"Game\":\"382bb353448f4c4d9637263518c085b9\", \"Player\":\"48d19c8b4419409a9a63dfd1c8152db2\", \"X\":2, \"Y\":4}"
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```