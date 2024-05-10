from django.shortcuts import render

from member.models import memberinsert, idcheck


# Create your views here.
def member(request):
    return render(request, "member/member.html")
def meminsert(request):
    addr = (
        request.POST['id'],
        request.POST['pwd'],
        request.POST['name'],
        request.POST['email'],
        request.POST['tel'],
        request.POST['addr']
    )
    #('mewmew', '123', '춘배', '123@mail.com', '123', '123')
    print(addr)
    print(type(addr))
    memberinsert(addr)
    return render(request, "member/success.html", {'name':request.POST['name']})

def memIdchk(request):
    idx = request.GET['id']
    res = idcheck(idx)
    print('id', res[0])
    return render(request, 'member/idchk.html', {'res':res[0]})