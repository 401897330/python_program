from django.shortcuts import render,redirect,HttpResponse
from Hosts.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils.md5 import encrypt
import json
from django import forms
from django.views import View
from django.forms import Form
from django.forms import fields
from django.forms import widgets


def auth(func):
    def inner(request,*args,**kwargs):
        ck = request.session.get("session_msg")
        if not ck:
            return redirect('/login/')
        return func(request,*args,**kwargs)
    return inner

class UserForm(Form):
    name = fields.CharField(
        required=True,
        #这里定义在attrs里面定义的name属性并不生效,默认html标签生成的name为当前字段名 即name="user"
        widget=forms.TextInput(attrs={"class":"form-control","type":"text", "placeholder":"输入字母或数字","id":"user_name","name":"user_name"}),
        error_messages={"required": "用户名不能为空！"}
    )
    password = fields.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "type": "password", "placeholder": "至少6位字母或数字",
            "id": "user_pwd", "name":"user_pwd"}),
        error_messages={"required": "密码不能为空！"}
    )

    re_password = fields.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "type": "password", "placeholder": "再次输入密码",
            "id": "re_user_pwd","name": "user_pwd"}),
        error_messages={"required": "此处不能为空！"}
    )

    e_mail = fields.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "type": "text", "placeholder": "例如:xxx@123.com", "id": "e_mail",}),
        error_messages={"required":"邮箱不能为空！","invalid":"邮箱格式错误"}
    )


    service = fields.MultipleChoiceField(
        choices=[],
        required=True,
        error_messages={"required":"至少选择一个"},
        widget=forms.SelectMultiple(attrs={"class": "form-control", "id":"service" }),
    )

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        print('===========>',Service.objects.values_list("id", "name"))
        self.fields['service'].choices = Service.objects.values_list("id", "name")

    '''
    自定义 检验字段，判断密码是否小于6位并且两次密码是否一样。
        如果我们希望验证form中的多个field, 
        或者验证涉及到已经存在之后的数据, 
        那么我们就需要用到form的clean()和clean_<field>&()方法了.
        其中需要注意的是, clean()和clean_<field>&()的最后必须返回验证完毕或修改后的值.
    '''

    def clean_name(self):
        name = self.cleaned_data['name']
        obj = User.objects.filter(name=name).first()
        if obj:
            raise forms.ValidationError("用户名已存在")
        return name


    def clean_password(self):
        password = self.cleaned_data['password']
        if str(password) < 6:
            raise forms.ValidationError("密码小于6位")
        return password


    #clean_"字段名" clean+下划线是对定义的单字段做判断，而且只能操作单字段，
    # clean方法则是在所有的单字段判断完之后再对整体所有的数据判断一次，可以对多字段操作
    def clean(self):
        print(self.cleaned_data)
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password == re_password:
            return self.cleaned_data
        else:
            from django.core.exceptions import ValidationError
            self.add_error("re_password", ValidationError("两次输入的密码不一致"))
            return self.cleaned_data


class HostForm(UserForm,Form):
    ip = fields.GenericIPAddressField(
        required=True,
        error_messages={"required": "IP不能为空！", "invalid": "IP格式错误"},
        widget = forms.TextInput(
        attrs={"class": "form-control", "type": "text", "placeholder": "例如:xxx@123.com", "id": "e_mail", }),
    )

    port = fields.CharField(
        required=True,
        error_messages={"required": "端口不能为空！"}
    )

    doman = fields.CharField(
        required=True,
        error_messages={"required": "域名不能为空！"}
    )



#
# class EdiView(View):
#     def post(self, request, *args, **kwargs):
#         form = HostForm(data=request.POST)
#         if form.is_valid():
#              Hosts.objects.filter(id=ID).update(**form.cleaned_data)
#         return redirect("/index/?page=%s" % page)


@auth
def ediHosts(request):
    ip = request.POST.get("ip")
    port = request.POST.get("port")
    doman = request.POST.get("doman")
    service = request.POST.get("service")
    service_id = Service.objects.get(name=service).id
    ID = request.POST.get("ID")
    page = request.POST.get("page").split("/")[2]
    if page:
        page = request.POST.get("page").split("=")[1].split('"')[0]
    else:
        page = 1
    Hosts.objects.filter(id=ID).update(ip=ip, port=port, doman=doman, service_line_id=service_id)
    return redirect("/index/?page=%s" % page)


@auth
def ediUser(request):
    name = request.POST.get("user_name")
    e_mail = request.POST.get("e_mail")
    service = request.POST.getlist("service")
    ID = request.POST.get("ID")
    page = request.POST.get("page").split("/")[2]
    if page:
        page = request.POST.get("page").split("=")[1].split('"')[0]
    else:
        page = 1
    obj = User.objects.filter(id=ID)
    obj[0].service.clear()
    obj.update(name=name, e_mail=e_mail)
    for i in service:
        service_name = Service.objects.get(name=i)
        obj[0].service.add(service_name)
    return redirect("/manager_user/?page=%s" % page)


#注册数据验证
class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, "register.html", locals())

    def post(self, request, *args, **kwargs):
        form = UserForm(data=request.POST)
        if form.is_valid():
            service_id_list = form.cleaned_data.pop("service")
            form.cleaned_data.pop("re_password")
            form.cleaned_data["password"] = encrypt(form.cleaned_data["password"])
            obj = User.objects.create(**form.cleaned_data)
            obj.service.add(*service_id_list)
            return render(request, "login.html", locals())
        else:
            return render(request, "register.html", locals())


class AuthView(object):
    def dispatch(self, request, *args, **kwargs):
        if request.session.get("session_msg"):
            response = super(AuthView, self).dispatch(request,*args,**kwargs)
            return response
        else:
            return redirect("/login/")


class IndexView(AuthView, View):
    def get(self,request,*args,**kwargs):
        try:
            ck = request.session.get("session_msg")
            all_service_list = Service.objects.all()
            hosts_list = Hosts.objects.all()
            keyword = request.GET.get("keyword")
            if keyword:
                num = Service.objects.filter(name__contains=keyword)
                hosts_list = Hosts.objects.filter(service_line_id=num)
            all_hosts_list = []
            for host in hosts_list:
                hosts_dic = {}
                hosts_dic["id"] = host.id
                hosts_dic["ip"] = host.ip
                hosts_dic["port"] = host.port
                hosts_dic["doman"] = host.doman
                service_queryset = Hosts.objects.filter(id=host.id).values("service_line_id__name")
                service = service_queryset[0]["service_line_id__name"] #这里的servie_line_id__name是去queryset的值
                hosts_dic["service"] = service
                all_hosts_list.append(hosts_dic)
            p = Paginator(all_hosts_list, 6)
            page = request.GET.get("page")
            page_num = range(1,11)
            if page:
                num1 = int(page) - 3
                start_num = num1
                end_num = int(page) + 5
                if end_num >= p.num_pages:
                    start_num = p.num_pages - 8
                    end_num = p.num_pages + 1
                page_num2 = range(start_num, end_num)
                page = int(page)
                if int(page) >= p.num_pages:
                    all_hosts_list = p.page(p.num_pages)
                else:
                    all_hosts_list = p.page(int(page))
            else:
                all_hosts_list = p.page(1)
            return render(request, "login.html", locals())
        except EmptyPage:
            all_hosts_list = all_hosts_list = p.page(1)
            return render(request, "login.html", locals())

@auth
def addHosts(request):
    ck = request.session.get("session_msg")
    all_service_list = Service.objects.all()
    if request.method == "POST":
        ip = request.POST.get("ip")
        port = request.POST.get("port")
        doman = request.POST.get("doman")
        service = request.POST.get("service")
        # 添加数据库
        service_id = Service.objects.get(name=service).id
        Hosts.objects.create(ip=ip, port=port, doman=doman, service_line_id=service_id)
        return redirect("/index/")
    return render(request, "addHosts.html", locals())

@auth
def addService(request):
    ck = request.session.get("session_msg")
    if request.method == "POST":
        name = request.POST.get("add_service")
        Service.objects.create(name=name)
        return redirect("/manager_service/")


@auth
def HostInfo(request):
    ck = request.session.get("session_msg")
    service_name = request.GET.get("name")
    user_queryset = Service.objects.filter(name=service_name).values("user__name", "user__e_mail")
    user_list = []
    for user in user_queryset:
        user_list.append(user)
    return render(request, "HostInfo.html", locals())


@auth
def delHosts(request):
    data = request.GET.get("data")
    id = data.split("/")[1]
    page = data.split("/")[3]
    Hosts.objects.filter(id=id).delete()
    return redirect("/index/%s" % page)


@auth
def delUser(request):
    data = request.GET.get("data")
    id = data.split("/")[1]
    page = data.split("/")[3]
    obj = User.objects.filter(id=id)[0]
    obj.service.clear()
    obj.delete()
    return redirect("/manager_user/%s" % page)


@auth
def delService(request):
    data = request.GET.get("data")
    id = data.split("/")[1]
    page = data.split("/")[3]
    hosts_dic = Service.objects.filter(id=id).values("hosts__id")
    for hosts_id in hosts_dic:
        print(hosts_id['hosts__id'])
        Hosts.objects.filter(id=hosts_id['hosts__id']).delete()
    Service.objects.filter(id=id).delete()
    return redirect("/manager_service/%s" % page)


def add(request):
    # 批量导入Hosts_user_service数据
    # import random
    # for i in range(1,5):
    #     user_obj = User.objects.get(id=i)
    #     num = random.randrange(0,3)
    #     author_list = Service.objects.all()[num:num+2]
    #     user_obj.service.add(*author_list)
    # return HttpResponse("OK")

    # 批量导入Hosts_hosts数据
    # Hostslist = []
    # import random
    # for i in range(1,201):
    #     num = random.randrange(1,5)
    #     Hostslist.append(Hosts(ip="192.168.1.%s" % i, port=22, doman="tvm%s.com"% i,service_line_id=num))
    # Hosts.objects.bulk_create(Hostslist)
    return HttpResponse("OK")


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user = request.POST.get("login_user")
        pwd = request.POST.get("login_pwd")
        pwd = encrypt(pwd)
        obj = User.objects.filter(name=user, password=pwd)
        if obj:
            request.session['session_msg'] = user
            return redirect("/index/page=1")
        else:
            msg = "用户名或密码错误！"
            return render(request, "login.html", locals())


#注销
@auth
def logout(request):
    request.session.clear()
    return redirect("/login/")


#用户管理页面
class ManagerUser(AuthView, View):
    def get(self, request, *args, **kwargs):
        try:
            ck = request.session.get("session_msg")
            all_service_list = Service.objects.all()
            users_list = User.objects.all()
            #user.service.all() 可以获取“user对象”的service的列表
            # for user in users_list:
            #     for service in user.service.all():
            #         print(service.id)

            p = Paginator(users_list, 6)
            page = request.GET.get("page")
            page_num = range(1, 11)
            if page:
                num1 = int(page) - 3
                start_num = num1
                end_num = int(page) + 5
                if end_num >= p.num_pages:
                    start_num = p.num_pages - 8
                    end_num = p.num_pages + 1
                page_num2 = range(start_num, end_num)
                page = int(page)
                if int(page) >= p.num_pages:
                    all_users_list = p.page(p.num_pages)
                else:
                    all_users_list = p.page(int(page))
            else:
                all_users_list = p.page(1)
            return render(request, "manager_user.html", locals())
        except EmptyPage:
            all_users_list = all_users_list = p.page(1)
            return render(request, "manager_user.html", locals())



class ManagerService(AuthView, View):
    def get(self, request, *args, **kwargs):
        try:
            ck = request.session.get("session_msg")
            all_service_list = Service.objects.all()
            p = Paginator(all_service_list, 6)
            page = request.GET.get("page")
            page_num = range(1, 11)
            if page:
                num1 = int(page) - 3
                start_num = num1
                end_num = int(page) + 5
                if end_num >= p.num_pages:
                    start_num = p.num_pages - 8
                    end_num = p.num_pages + 1
                page_num2 = range(start_num, end_num)
                page = int(page)
                if int(page) >= p.num_pages:
                    all_service_list = p.page(p.num_pages)
                else:
                    all_service_list = p.page(int(page))
            else:
                all_service_list = p.page(1)
            return render(request, "manager_service.html", locals())
        except EmptyPage:
            all_service_list = all_service_list = p.page(1)
            return render(request, "manager_service.html", locals())


