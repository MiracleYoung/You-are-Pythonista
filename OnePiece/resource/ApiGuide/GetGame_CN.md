## 获取游戏详细

### URL
http://test.magcore.clawit.com/api/game/{GameId}

{GameId}: 欲获取信息的游戏Id

### Method
GET

### 返回结果
Status Code: 200

Content:
```json
{
	"Id": "ce71d669e4d141a298472591de92f8e6",
	"Map": "RectSmall",
	"State": 0,
	"Players": [
        {
            "Index": 5,
            "Color": 1,
            "Name": "cc",
            "State": 1
        }
    ],
	"Cells": [
		[{
				"X": 0,
				"Y": 0,
				"Type": 0,
				"State": 0,
				"Owner": 0
			},
			{
				"X": 1,
				"Y": 0,
				"Type": 1,
				"State": 0,
				"Owner": 0
			}
		],
		[{
				"X": 0,
				"Y": 1,
				"Type": 1,
				"State": 0,
				"Owner": 0
			},
			{
				"X": 1,
				"Y": 1,
				"Type": 0,
				"State": 0,
				"Owner": 0
			}
		]
	]
}
```

Id: 游戏Id

Map: 游戏所用地图名称

State: 游戏当前状态

Players: 当前游戏中的玩家**数组**
  - Index: 玩家的标识号
  - Color: 玩家的颜色
  - Name: 玩家昵称
  - State: 玩家状态

Cells: 游戏所有单元的状态**二维数组**
  - X: 单元的x坐标
  - Y: 单元的y坐标
  - Type: 单元的类型
  - State: 单元的状态
  - Owner: 单元所属的玩家标识号

### 示例
#### Python
```python
import requests

url = "http://test.magcore.clawit.com/api/game/ce71d669e4d141a298472591de92f8e6"

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
  "url": "http://test.magcore.clawit.com/api/game/ce71d669e4d141a298472591de92f8e6",
  "method": "GET",
  "headers": {
    "Cache-Control": "no-cache"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```