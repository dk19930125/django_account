from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect  

from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from .models import BBS

# Create your views here.
def index(request):
    bbs_list = BBS.objects.all()

    return render(request,'index.html',{'bbs_list':bbs_list})

def bbs_detail(request,bbs_id):
    bbs = BBS.objects.get(id=bbs_id)
    return render(request,"bbs_detail.html",{'bbs_obj':bbs})

@login_required(login_url='/login/')
def comment(request):
    return HttpResponse("comment")

def login_w(request,):

    return render(request,'login.html')

def auth(request):
    username, passwd = request.POST['username'],request.POST['passwd']
    users = authenticate(username=username, password=passwd)

    if users is not None:
        login(request,users)
        response = HttpResponseRedirect('/')
        # response.set_cookie('username',username,2)
        return response
    else:
        return HttpResponseRedirect('/login/')

def logout_w(request):
    logout(request)
    return HttpResponseRedirect("/")

# 