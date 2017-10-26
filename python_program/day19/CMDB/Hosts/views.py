from django.shortcuts import render,redirect,HttpResponse
from django.forms.models import model_to_dict
from Hosts.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils.md5 import encrypt
import json

# Create your views here.1

def auth(func):
    def inner(request,*args,**kwargs):
        ck = request.session.get("session_msg")
        if not ck:
            return redirect('/login/')
        return func(request,*args,**kwargs)
    return inner

@auth
def index(request):
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
def HostInfo(request):
    ck = request.session.get("session_msg")
    service_name = request.GET.get("name")
    user_queryset = Service.objects.filter(name=service_name).values("user__name", "user__e_mail")
    user_list = []
    for user in user_queryset:
        user_list.append(user)
    print(user_list)
    return render(request, "HostInfo.html", locals())



def delHosts(request):
    data = request.GET.get("data")
    id = data.split("/")[1]
    page = data.split("/")[3]
    Hosts.objects.filter(id=id).delete()
    return redirect("/index/%s" % page)


@auth
def ediHosts(request):
    ip = request.POST.get("ip")
    port = request.POST.get("port")
    doman = request.POST.get("doman")
    service = request.POST.get("service")
    service_id = Service.objects.get(name=service).id
    ID = request.POST.get("ID")
    page = request.POST.get("page").split("=")[1].split('"')[0]
    Hosts.objects.filter(id=ID).update(ip=ip, port=port, doman=doman, service_line_id=service_id)
    return redirect("/index/?page=%s" % page)

@auth
def add(request):
    # 批量导入Hosts_user_service数据
    # import random
    # for i in range(1,5):
    #     user_obj = User.objects.get(id=i)
    #     num = random.randrange(0,3)
    #     author_list = Service.objects.all()[num:num+2]
    #     user_obj.service.add(*author_list)
    return HttpResponse("OK")

    # 批量导入Hosts_hosts数据
    # Hostslist = []
    # import random
    # for i in range(200):
    #     num = random.randrange(1,5)
    #     Hostslist.append(Hosts(ip="192.168.1.%s" % i, port=22, doman="tvm%s.com"% i,service_line_id=num))
    # Hosts.objects.bulk_create(Hostslist)
    # return HttpResponse("OK")


def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        user = request.POST.get("login_user")
        pwd = request.POST.get("login_pwd")
        pwd = encrypt(pwd)
        obj = User.objects.filter(name=user, password=pwd)
        print(user,pwd)
        if obj:
            request.session['session_msg'] = user
            return redirect("/index/")
        else:
            msg = "用户名或密码错误！"
            return render(request, "login.html", locals())


#注销
def logout(request):
    request.session.clear()
    return redirect("/login/")



#注册数据验证

def register(request):
    all_service_list = Service.objects.all()
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_pwd = request.POST.get("password")
        re_user_pwd = request.POST.get("re_password")
        e_mail = request.POST.get("email")

        service_list = request.POST.get("service_list").split(',')

        user_list = User.objects.filter(name=user_name).first()
        pwd_num = len(str(user_pwd))
        dic = {"flag": False}
        if user_pwd != re_user_pwd or user_list or not service_list or pwd_num < 6:
            dic = {"flag": True}
            return HttpResponse(json.dumps(dic))
        User.objects.create(name=user_name, password=encrypt(user_pwd), e_mail=e_mail)
        user_id = User.objects.all().last().id
        user_obj = User.objects.get(id=user_id)
        for name in service_list:
            service_obj = Service.objects.get(name=name)
            user_obj.service.add(service_obj)
        return HttpResponse(json.dumps(dic))
    return render(request, "register.html",locals())


#ajax后台验证用户名，密码是否符合要求

def valiname(request):
    user = request.POST.get("user")
    user_list = User.objects.filter(name=user).first()
    dic = {"flag": False}
    if user_list:
        dic = {"flag": True}
        return HttpResponse(json.dumps(dic))
    return HttpResponse(json.dumps(dic))


def valipwd(request):
    pwd = request.POST.get("password")
    pwd_num = len(str(pwd))
    dic = {"flag": False}
    if pwd_num < 6:
        dic = {"flag": True}
        return HttpResponse(json.dumps(dic))
    return HttpResponse(json.dumps(dic))


def valirepwd(request):
    pwd = request.POST.get("password")
    re_pwd = request.POST.get("re_password")
    dic = {"flag": False}
    print(pwd,re_pwd)
    if pwd != re_pwd:
        dic = {"flag": True}
        return HttpResponse(json.dumps(dic))
    return HttpResponse(json.dumps(dic))