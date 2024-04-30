from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from django.http import JsonResponse
import time
from django.views.decorators.csrf import csrf_exempt
from app1.models import Student
import json
from django.db.models import F,Q,Avg,Count,Max,Min,Sum

@csrf_exempt
# Create your views here.
def time1(request):
    # return HttpResponse('time1')
    time1st = time.strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'app01/index.html',{"shijian": time1st})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        if username == 'username' and password == 'password':
            return redirect('/time1/')
        else:
            return HttpResponse('用户登录失败')
    else:
        return render(request, 'app01/login.html')


@csrf_exempt
def add_stu(request):
    # s1 = Student(name = 'hahahhaheiheihei',age=21,birthday='1996-05-02',ismarired=False)
    # print(s1.id)
    # s1.save()
    # print(s1.id)
    s2 = Student.objects.create(name = 'tian',age=22,birthday='1996-01-02',ismarired=False)

    return HttpResponse('add_stu')


@csrf_exempt
def selectall(request):
    s1 = Student.objects.all().values("name","id","age").distinct()
    print(s1)
    # print(s1[2].name)
    # for i in s1:
    #     print(i.name,i.id)
    # s2 = Student.objects.filter(age = 21)
    # print(s2)
    # s3 = Student.objects.get(id = 1)
    # print(s3.name)


@csrf_exempt
def delete_stu(reuqest,del_id):
    # Student.objects.filter(id = del_id).delete()
    try:
        Student.objects.get(id = del_id).delete()
    except :
        return HttpResponse('删除失败')

    return HttpResponse('删除成功')


@csrf_exempt
def select2(request):
    # result = Student.objects.filter(age__gt =21).values("name")
    # result = Student.objects.filter(birthday__day=2).values("name")
    # result = Student.objects.filter(height__gt=F("weight")).values("name")
    # result = Student.objects.filter(Q(height__gt=170)&Q(age__gt=20)).values("name")
    # result = Student.objects.all().aggregate(Max("age"))
    result  = Student.objects.all().values("class_name").annotate(Max("height"))
    return HttpResponse(json.dumps(list(result)))