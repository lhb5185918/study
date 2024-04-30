"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import time

from django.contrib import admin
from django.urls import path,re_path,include
from app1 import views as v1
from app2 import views as v2


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('time1/',include('app1.urls')),
    # # re_path('^selectnumber/(\d{4})$',v1.selectnumber),
    # # re_path('selectnumber/(^?p<year>\d{4})/(^?p<month>\d{2})',v1.selectnumber),
    # path('selectnumber/',include('app1.urls')),
    path('',v2.index),
    path('login/',v1.login_view),
    path('time1/',v1.time1),
    path('addstu/',v1.add_stu),
    path('selectall/',v1.selectall),

]
