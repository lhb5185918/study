from django.contrib import admin
from django.urls import path,re_path
from app1 import views as v1




urlpatterns = [
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})$',v1.selectnumber),
    # path('',v1.time1),
]