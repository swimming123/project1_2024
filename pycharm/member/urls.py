from django.urls import path

from member import views

urlpatterns=[
    path('member', views.member),
    path('meminsert', views.meminsert),
    path('memIdchk', views.memIdchk),
]