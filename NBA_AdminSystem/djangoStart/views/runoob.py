from django.shortcuts import render
from djangoStart.sms import MySmsSender

def runoob(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['name'] = "name"
    context['list'] = ["a" , "b" , "c"]
    context['num'] = 3
    context['str'] = "<a href='https://www.runoob.com/'>点击跳转</a>"
    views_name = "hhh"
    views_hello = "hello world"
    views_list = [1 , 2 , 3]
    views_dict = {"e1" : 1 }
    # 测试短信发送
    #smsSender = MySmsSender()
    #smsSender.send("18033165031", "1280857", "123456")
    return render(request, 'sample.html', context)

