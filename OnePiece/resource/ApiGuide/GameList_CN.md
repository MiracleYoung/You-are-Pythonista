## 获取游戏列表

### URL
http://test.magcore.clawit.com/api/game

### Method
GET


### 返回结果
Status Code: 200

Content: 
返回所有游戏的**数组**

```json
[
    {
        "id": "ce71d669e4d141a298472591de92f8e6",
        "map": "RectSmall",
        "state": 0
    }
]
```

id: 游戏Id

map: 所用的地图

state: 游戏当前状态

### 示例
#### Python
```python
import requests

url = "http://test.magcore.clawit.com/api/game"

headers = {
    'Cache-Control': "no-cache",
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
```

#### JavaScript
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://test.magcore.clawit.com/api/game",
  "method": "GET",
  "headers": {
    "Cache-Control": "no-cache"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```