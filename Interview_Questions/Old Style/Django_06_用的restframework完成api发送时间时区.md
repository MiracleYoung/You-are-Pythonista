# Django_06_用的 restframework 完成 api 发送时间时区


## Question
用的 restframework 完成 api 发送时间时区

----

## Answer
```python
class getCurrenttime(APIView):
    def get(self,request):
        local_time = time.localtime()
        time_zone =settings.TIME_ZONE
        temp = {'localtime':local_time,'timezone':time_zone}
        return Response(temp)
```