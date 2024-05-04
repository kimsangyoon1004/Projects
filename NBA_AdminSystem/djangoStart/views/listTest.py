from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from TestModel.models import Test


def list(request):
    Test_list = Test.objects.all()
    print(Test_list)
    paginator = Paginator(Test_list , 2)
    page = request.GET.get('page')
    try:
        Tests = paginator.page(page)
    except PageNotAnInteger:
        Tests = paginator.page(1)
    except EmptyPage:
        #返回最后一页
        Tests = paginator.page(paginator.numpages)
    ctx = {}
    ctx['Tests'] = Tests
    return render(request, 'listTest.html' , ctx)

