from django.shortcuts import render, redirect, HttpResponse
from BoxInfo import models
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json,os,time,datetime
from django import forms
from django.views import View
from django.forms import Form
from django.forms import fields
from django.forms import widgets
import requests
from django.db import transaction
from django.http import QueryDict
import logging

# Create your models here.

#分页器函数
def page_burster(current_page, all_box_info):
    per_page = 20
    all_count = all_box_info.count()
    pager_count, b = divmod(all_count, per_page)
    if b != 0:
        pager_count += 1
    start = (current_page - 1) * per_page
    end = current_page * per_page
    all_data = all_box_info[start:end]

    if pager_count <= 10:
        page_start = 1
        page_end = pager_count
    else:
        if current_page <= 4:
            page_start = 1
            page_end = 10
        else:
            if (current_page + 5) > pager_count:
                page_end = pager_count
                page_start = pager_count - 9
            else:
                page_start = current_page - 4
                page_end = current_page + 5
    page_list = []
    if current_page <= 1:
        prve = '<a style="width: 80px">上一页</a>'
    else:
        prve = '<a style="width: 80px" href="/suntv/index?page=%s">上一页</a>' % (current_page - 1)
    page_list.append(prve)
    for i in range(page_start, page_end + 1):
        if current_page == i:
            tpl = '<a class="active" href="/suntv/index?page=%s">%s</a>' % (i, i)
        else:
            tpl = '<a href="/suntv/index?page=%s">%s</a>' % (i, i)
        page_list.append(tpl)
    if current_page >= pager_count:
        last = '<a style="width: 80px">下一页</a>'
    else:
        last = '<a style="width: 80px" href="/suntv/index?page=%s">下一页</a>' % (current_page + 1)
    page_list.append(last)
    page_str = "".join(page_list)
    return all_data, page_str, pager_count


def auth(func):
    def inner(request,*args,**kwargs):
        ck = request.session.get("session_msg")
        if not ck:
            return redirect('/login/')
        return func(request, *args, **kwargs)
    return inner


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user = request.POST.get("login_user")
        pwd = request.POST.get("login_pwd")
        obj = models.UserInfo.objects.filter(username=user, password=pwd)
        if obj:
            request.session['session_msg'] = user
            print('ok')
            return redirect("/suntv/index?page=1")
        else:
            msg = "用户名或密码错误！"
            return render(request, "login.html", locals())


@csrf_exempt
def box_info(request):
    try:
        data = request.body.decode("utf-8")
        if data:
            box_logs = eval(data)["data"]
            data = []
            for log in box_logs:
                log["request_time"] = datetime.datetime.strptime(log["request_time"], '%Y-%m-%d %H:%M:%S')
                data.append(models.BoxInfo(**log))
            models.BoxInfo.objects.bulk_create(data)
    except Exception as e:
        return HttpResponse("403")
    else:
        return HttpResponse("GET MSG")

@auth
def index(request):
    if request.method == "POST":
        try:
            keyword = request.POST.get("keyword")
            if request.POST.get("start_time"):
                start_time = "%s 00:00:00" % request.POST.get("start_time")
            else:
                now_time = datetime.datetime.now()
                yes_time = now_time + datetime.timedelta(days=-1)
                start_time = "%s 00:00:00" % yes_time.strftime('%Y-%m-%d')
            if request.POST.get("end_time"):
                end_time = "%s 00:00:00" % request.POST.get("end_time")
            else:
                now = datetime.datetime.now()
                end_time = now.strftime('%Y-%m-%d %H:%M:%S')
            time_start = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            time_end = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

            request.session['keyword'] = keyword
            request.session['start_time'] = start_time
            request.session['end_time'] = end_time

            all_box_info = models.BoxInfo.objects.filter(sn=keyword, request_time__gt=time_start, request_time__lt=time_end)
            current_page = 1
            all_data, page_str, pager_count = page_burster(current_page, all_box_info)
        except Exception as e:
            return HttpResponse("404")
        else:
            return render(request, "index.html", locals())
    else:
        try:
            keyword = request.session.get("keyword")
            start_time = request.session.get("start_time")
            end_time = request.session.get("end_time")
            if keyword and start_time and end_time:
                time_start = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
                time_end = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
                all_box_info = models.BoxInfo.objects.filter(sn=keyword, request_time__gt=time_start, request_time__lt=time_end)
            else:
                all_box_info = models.BoxInfo.objects.all()
            current_page = request.GET.get("page")
            if not current_page:
                current_page = 1
            else:
                current_page = int(current_page)
            all_data, page_str, pager_count = page_burster(current_page, all_box_info)
        except Exception as e:
            return HttpResponse("404")
        else:
            return render(request, "index.html", locals())


@auth
def logout(request):
    request.session.clear()
    return redirect("/login/")


logger = logging.getLogger("__name__")   # 生成一个以当前模块名为名字的logger实例
c_logger = logging.getLogger("collect")  # 生成一个名为'collect'的logger实例，用于收集一些需要特殊记录的日志

