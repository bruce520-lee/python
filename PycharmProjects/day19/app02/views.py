from django.shortcuts import render,HttpResponse,redirect
from app02 import models
# Create your views here.



def login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        obj = models.login.objects.filter(username=u,password=p).first()
        # print(obj.id,obj.username,obj.password)
        # for row in obj:
        #     print(row.id,row.username,row.password)
        print(obj)
        if obj:
            return render(request,'index1.html')
        else:
            error_msg = "Invalid!"
            return render(request,'login.html',{'error_msg':error_msg})
    return render(request,'login.html')


def orm(request):
    #-----------增----------------
    # dict = {
    #     'username':'alex',
    #     'password':'888'
    # }
    # models.login.objects.create(**dict)
    # print(models.Info.objects)
    # result = models.login.objects.all()
    models.login.objects.filter(id=1).delete()
    models.login.objects.all().update(username='alex')
    models.login.objects.filter(id=2).update(id=1)
    result = models.login.objects.filter(username='root',password='123')
    print(result)
    for row in result:
        print(row.id,row.username,row.password)

    return HttpResponse('ORM')


def user_list(request):
    return render(request,'user_list.html')

def user_info(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.login.objects.create(username=u,password=p)
        return redirect('/cmdb/user_info/')
    elif request.method == 'GET':
        obj = models.login.objects.all()
        # fir = models.login.objects.filter(id=1).first()
        # print(fir.id,fir.username,fir.password)
        return render(request,'user_info.html',{'user_info':obj})
    # return HttpResponse('hello')

def userdel(request,nid):
    models.login.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info')

def user_detail(request,nid):
    print(nid)
    obj = models.login.objects.filter(id=nid).first()
    print(obj.id, obj.username, obj.password)
    return render(request,'user_detail.html',{'obj':obj})

def useredit(request,nid):
    if request.method == 'GET':
        obj1 = models.login.objects.filter(id=nid).first()
        return render(request,'user_edit.html',{'obj':obj1})
    elif request.method == 'POST':
        # nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        print(nid,u,p)
        models.login.objects.filter(id=nid).update(username=u,password=p)
        return redirect('/cmdb/user_info')