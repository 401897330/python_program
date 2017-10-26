from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
from app01 import models


class AuthView(object):
    def dispatch(self, request, *args, **kwargs):
        if request.session.get('user_info'):
            response = super(AuthView,self).dispatch(request, *args, **kwargs)
            return response
        else:
            return redirect('/login.html')
# FBV、CBV
class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView,self).dispatch(request, *args, **kwargs)

    def get(self, request, *args,**kwargs):
        return render(request,'login.html')

    def post(self,request, *args,**kwargs):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if obj:
            request.session['user_info'] = {'id':obj.id,'username': obj.username}
            return redirect('/users.html')
        return render(request, 'login.html',{'msg': '去你的'})

class UsersView(AuthView,View):

    def get(self,request,*args,**kwargs):
        user_list = models.UserInfo.objects.all()
        return render(request,'users.html',{'user_list':user_list})

class AddUserView(AuthView,View):
    def get(self,request,*args,**kwargs):
        return render(request,'add_user.html')












