## 开始游戏

### URL
http://test.magcore.clawit.com/api/game/{GameId}

{GameId}: 欲开始的游戏Id

### Method
PUT

### 返回结果
成功 Status Code: 200

失败 Status Code: 403

### 示例
#### Python
```python
import requests

url = "http://test.magcore.clawit.com/api/game/dcc83423fba04460a4d6b28fe6da4142"

headers = {
    'Cache-Control': "no-cache"
    }

response = requests.request("PUT", url, headers=headers)

print(response.text)
```

#### JavaScript
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://test.magcore.clawit.com/api/game/dcc83423fba04460a4d6b28fe6da4142",
  "method": "PUT",
  "headers": {
    "Cache-Control": "no-cache"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```