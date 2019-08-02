# Django_06_用的 restframework 完成 api 发送时间时区

## Question
用的 restframework 完成 api 发送时间时区

class getCurrenttime(____):
    def get(self,request):
        local_time = time.localtime()
        time_zone =____.____
        temp = {'localtime':local_time,'timezone':time_zone}
        return ____(temp)

%!A. Response, settings, TIME_ZONE, APIView!%

%!B. APIView, settings, TIME_ZONE, Response!%

%!C. Response, settings, APIView, TIME_ZONE!%

%!D. APIView, TIME_ZONE, settings, Response!%

----

## Answer
@!B!@

----

## Analysis

```python
class getCurrenttime(APIView):
    def get(self,request):
        local_time = time.localtime()
        time_zone =settings.TIME_ZONE
        temp = {'localtime':local_time,'timezone':time_zone}
        return Response(temp)
```

