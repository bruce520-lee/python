from django.shortcuts import render

# Create your views here.


from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from cmdb import models
# def login(request):
#     return HttpResponse('CMDB')


def submit(request):
    print(request.method)
    error_message = ""
    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        if username == 'root' and password == '123':
            return redirect("/home/")
        else:
            error_message = "Invalid Password!"
    return render(request,'login.html',{'error_message': error_message})

USER_LIST = [

]
def home(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        # temp = {'username':u,'email':e,'gender':g}
        # USER_LIST.append(temp)
        print('haha'.center(50,'-'))
        models.UserInfo.objects.create(username=u,email=e,gender=g)
        print('haha'.center(100, '-'))
        global USER_LIST
        USER_LIST = models.UserInfo.objects.all()
    print('usr_list%s'.center(50,'-')%USER_LIST)
    return render(request,'home.html',{'user_list':USER_LIST})

def submitfile(request):
    if request.method == 'POST':
        obj = request.FILES.get('filename')
        print(obj,obj.name,type(obj),'-------------------')
        f = open(obj.name,mode='wb')
        print(f,'----------------')
        for i in obj.chunks():
            f.write(i)
        f.close()
    return render(request,'submitfile.html')