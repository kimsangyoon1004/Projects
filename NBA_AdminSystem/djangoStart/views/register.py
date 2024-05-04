from django.shortcuts import render,HttpResponse
from TestModel import models
from djangoStart.sms import MySmsSender

def register(request):
    return render(request , 'register.html' )


def register_veri(request):
    if request.POST :
        phone_number = request.POST["phone_number"]
        smsSender = MySmsSender()
        smsSender.send(phone_number , "1280857" , "123456")
        _id = request.POST.get("id")
        _password = request.POST.get("password")
        _phone_number = request.POST["phone_number"]
        user = models.Test(id=_id , password=_password , phone_num=_phone_number  )
        user.save()

    return render(request , 'veri_register.html' )

def register_res(request):
    if request.POST:
        veri_code = request.POST["veri_code"]
    if veri_code == "123456":
        return HttpResponse("<p> 注册成功 </p>")
    else:
        return HttpResponse("<p> 验证码错误 </p>")
