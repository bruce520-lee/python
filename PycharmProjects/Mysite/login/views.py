from django.shortcuts import render
from login import models
from django.shortcuts import HttpResponse

# Create your views here.

# user_list = []

def index(request):
    #return HttpResponse('Hello World!')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        models.UserInfo.objects.create(user=username,pwd=password)
        print(username,password)
        # temp = {'user': username, 'password': password}
        # user_list.append(temp)
        # print(user_list)
    user_list = models.UserInfo.objects.all()
    return render(request,'index.html',{'data': user_list})

def submitfile(request):
    if request.method == 'POST':
        f = request.FILES.get('filename')
        print(f,f.name,type(f),'-------------------')
        f = open(f.name,mode='wb')
        for i in f.chunks():
            f.write(i)
        f.close()
    return render(request,'submitfile.html')