## 获取地图信息

### URL
http://test.magcore.clawit.com/api/map/{name}

{name}: 欲获取地图的名称

### Method
GET

### 返回结果
成功 Status Code: 200

失败 Status Code: 404

Content: 
```json
{
    "Edge": 4,
    "Shift": 0,
    "Direction": 0,
    "Rows": [
        "0111111111",
        "1000111111",
        "1011111111",
        "1111111111",
        "1111111111",
        "1111111111",
        "1111111111",
        "1111111101",
        "1111110001",
        "1111111110"
    ]
}
```

Edge: 单元的形状(暂保留)

Shift: 单元是否错误(暂保留)

Direction: 单元的朝向(暂保留)

Rows: 各单元类型的**数组**

### 示例
#### Python
```python
import requests

url = "http://test.magcore.clawit.com/api/map/rectsmall"

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
  "url": "http://test.magcore.clawit.com/api/map/rectsmall",
  "method": "GET",
  "headers": {
    "Cache-Control": "no-cache"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```