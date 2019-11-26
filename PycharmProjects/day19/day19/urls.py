"""day19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    url(r'^cmdb/',include('app02.urls')),
    # url(r'^login/',views.login),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # url('index/',views.index),
#     # url('submitfile/',views.submitfile),
#     # url('home/',views.Home.as_view()),
#     url(r'^login',views.login),
#     # url(r'^detail',views.detail),
#     # url(r'^detail-(\d+).html',views.detail),
#     url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html',views.detail),
#     url(r'^jump',views.jump)
# ]
