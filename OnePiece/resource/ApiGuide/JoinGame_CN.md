## 加入游戏

### URL
http://test.magcore.clawit.com/api/game

### Method
PATCH

### Header
Content-Type: application/json

### Body
```json
{
	"Game": "1b0aa68195de4a2ba5a43437672dc56a",
	"Player": "a8fe42fd032e45f2bc9579e573d89f06"
}
```

Game: 欲参加的游戏Id

Player: 自己作为玩家的Id


### 返回结果
成功 Status Code: 200

失败 Status Code: 403

### 示例
#### Python
```python
import requests

url = "http://test.magcore.clawit.com/api/game/"

payload = "{\"Game\":\"1b0aa68195de4a2ba5a43437672dc56a\", \"Player\":\"a8fe42fd032e45f2bc9579e573d89f06\"}"
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)
```

#### JavaScript
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://test.magcore.clawit.com/api/game/",
  "method": "PATCH",
  "headers": {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache"
  },
  "processData": false,
  "data": "{\"Game\":\"1b0aa68195de4a2ba5a43437672dc56a\", \"Player\":\"a8fe42fd032e45f2bc9579e573d89f06\"}"
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```