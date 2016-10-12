from django.shortcuts import render
from django import forms
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from .models import User
class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def Regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username=username,password=password)
            # print username,password
            return HttpResponseRedirect("/user/login/")

    else:
        uf = UserForm()
    return render(request,'regist.html',{'uf':uf})

def Login(request):

    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            users = User.objects.filter(username__exact=username,password__exact=password)
            # print "uuuuuuuu",users
            if users:

                response = HttpResponseRedirect("/user/index/")
                response.set_cookie("username",username,10)
                return response
            else:
                return HttpResponseRedirect('/user/login/')
    else:
        uf = UserForm()
    return render(request,'regist.html',{'uf':uf})



def Index(request):
    username = request.COOKIES.get('username','')
    return HttpResponse("weclome %s" % username)
def Logout(request):
    response = HttpResponse('Logout')
    response.delete_cookie("username")
