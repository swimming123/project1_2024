from django.shortcuts import render
def mainHome(request):
    return render(request,"main.html")