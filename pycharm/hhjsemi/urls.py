from django.urls import path

from hhjsemi import views

urlpatterns=[
    path('projectList',views.projectList),
    path('projectTitle',views.projectTitle),
]