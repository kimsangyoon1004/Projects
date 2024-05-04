"""djangoStart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import xadmin
#from django.conf.urls import url
from . import testdb,search,infoFeedback , weatherPredict , testInsert, testRes
from .views import runoob , register , listTest

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('listTest/' , listTest.list),
    path('register_res/' , register.register_res),
    path('register_veri/' , register.register_veri),
    path('register/', register.register),
    path('submitResult/' , infoFeedback.subRes),
    path('submit/' , infoFeedback.submit),

    path('weatherPredict/' , weatherPredict.search ),

    path('showResult/' , search.showRes2),
    path('search/' , search.search),
    path('testdb/' , testdb.testdb),
    path('runoob/', runoob.runoob),
    #path('admin/', admin.site.urls),
    path('NBADBadmin/', xadmin.site.urls),

    path("DBInsert/", testInsert.insert),
    path("DBRes/", testRes.showRes),
] 
