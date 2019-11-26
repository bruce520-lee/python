from django.shortcuts import render,HttpResponse
from app01 import models
import os
# Create your views here.
from django.core.files.uploadedfile import InMemoryUploadedFile

# def index(reqest):
#     return HttpResponse('Hello')


# user_dict = {
#     'k1' : 'root1',
#     'k2' : 'root2',
#     'k3' : 'root3',
# }

user_dict = {
    '1' : {'username':'root1','email':'root1@qq.com'},
    '2' : {'username':'root2','email':'root2@qq.com'},
    '3' : {'username':'root3','email':'root3@qq.com'},
}




def login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        # models.UserInfo.objects.create(usernmae=u,email=e)
        user_list = []
        temp = {'username':u,'email':e}
        user_list.append(temp)
        print(user_list)
    return render(request,'login.html',{'data':user_dict})

def detail(request,*args,**kwargs):
    # nid = request.GET.get('nid')
    # detail_info = user_dict[nid]
    # return render(request,'detail.html',{'detail_info':detail_info})
    # if request.method == 'GET':
    # print('-------d------',type(request))
    # nid = request.GET.get('nid')
    # print(nid)
    # detail_info = user_dict[nid]
    # print(detail_info)
    # return render(request,'detail.html',{'detail_info':detail_info})
    print(kwargs)
    a = []
    for k in kwargs:
        a.append(k)
    print(a)
    return HttpResponse(kwargs[a[0]])


def jump(request):
    print(user_dict)
    return render(request,'jump.html',{'user_dict':user_dict})



# def index(request):
#     if request.method == 'POST':
#         g = request.POST.get('gender')
#         print(g)
#         f = request.POST.getlist('favor')
#         print(f)
#     return render(request,'index.html')
#
# def submitfile(request):
#     if request.method == 'POST':
#         obj = request.FILES.get('filename')
#         print(obj,obj.name,type(obj),'-------------------')
#         file_path = os.path.join('upload',obj.name)
#         print(file_path)
#         f = open(file_path,mode='wb')
#         for i in obj.chunks():
#             f.write(i)
#         f.close()
#     return render(request,'submitfile.html')

# from django.views import View
# class Home(View):
#     def dispatch(self, request, *args, **kwargs):
#
#
#     def get(self,request):
#         print(request.method)
#         return render(request,'home.html')
#     def post(self,request):
#         print(request.method)
#         return render(request,'home.html')


def user_list(request):
    pass