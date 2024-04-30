from django.shortcuts import render
from django.shortcuts import HttpResponse



# Create your views here.
def index(request):
    print(request.method)
    print(request.path)
    print(request.get_full_path())
    print(str(request.META).encode('utf-8'))
    print(request.GET)
    return HttpResponse('ok')