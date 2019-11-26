from django.urls import path
from django.conf.urls import url,include
from app02 import views

urlpatterns = [
    url(r'^login',views.login),
    url(r'^orm/',views.orm),
    url(r'^user_list/',views.user_list),
    url(r'^user_info/',views.user_info),
    url(r'^userdetail-(?P<nid>\d+)/',views.user_detail),
    url(r'^userdel-(?P<nid>\d+)/',views.userdel),
    url(r'^useredit-(?P<nid>\d+)/',views.useredit),
]