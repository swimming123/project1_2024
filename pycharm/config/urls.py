"""
URL configuration for config project.

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
from django.contrib import admin
from django.urls import path, include

from config import views

#http://localhost:9000/admin
#http://localhost:9000/address
urlpatterns = [
    path('admin/', admin.site.urls),
    path('address/', include('address.urls')),
    path('member/', include('member.urls')),
    path('myshop/', include('myshop.urls')),
    path('survey/', include('survey.urls')),
    path('',views.mainHome),
    path('login/',include('login.urls')),
    path('wordcnt/',include('wordcnt.urls')),
    path('resnet1/',include('resnet1.urls')),
    path('resapi/',include('resapi.urls')),
    path('semiprj/',include('semiprj.urls')),
    path('project/', include('project.urls')),
    path('project101/', include('project101.urls')),
    path('hhjsemi/', include('hhjsemi.urls')),

]