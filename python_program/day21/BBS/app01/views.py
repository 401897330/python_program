from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils.md5 import encrypt
from utils.response import BaseResponse,LikeResponse
import json,os,time
from django import forms
from django.views import View
from django.forms import Form
from django.forms import fields
from django.forms import widgets
import requests
from bs4 import BeautifulSoup
from django.db.models import F
from django.db import transaction


# Create your views here
def auth(func):
    def inner(request,*args,**kwargs):
        ck = request.session.get("session_msg")
        if not ck:
            return redirect('/login/')
        return func(request,*args,**kwargs)
    return inner


class UserForm(Form):
    username = fields.CharField(
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
        if len(str(password)) < 6:
            raise forms.ValidationError("密码小于6位")
        return password


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



def index(request, *args, **kwargs):
    try:
        ck = request.session.get("session_msg")
        current_new_type_id = kwargs.get('new_type_id')
        if current_new_type_id:
            current_new_type_id = int(current_new_type_id)
        news_list = models.News.objects.filter(**kwargs)
        news_type_list = models.NewsType.objects.all()

        p = Paginator(news_list, 6)
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
                news_list = p.page(p.num_pages)
            else:
                news_list = p.page(int(page))
        else:
            news_list = p.page(1)
        return render(request, "login.html", locals())
    except EmptyPage:
        news_list = news_list = p.page(1)
        return render(request, "login.html", locals())




class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user = request.POST.get("login_user")
        pwd = request.POST.get("login_pwd")
        pwd = encrypt(pwd)
        obj = models.UserInfo.objects.filter(username=user, password=pwd)
        if obj:
            request.session['session_msg'] = user
            return redirect("/index/page=1")
        else:
            msg = "用户名或密码错误！"
            return render(request, "login.html", locals())

@auth
def logout(request):
    request.session.clear()
    return redirect("/index/")


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, "register.html", locals())

    def post(self, request, *args, **kwargs):
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.cleaned_data.pop("re_password")
            form.cleaned_data["password"] = encrypt(form.cleaned_data["password"])
            obj = models.UserInfo.objects.create(**form.cleaned_data)
            return render(request, "login.html", locals())
        else:
            return render(request, "register.html", locals())

@auth
def get_title(request):
    url = request.POST.get("url")
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    desc = soup.find('meta', attrs={'name':'description'}).get('content')
    dic = {"title":title, "desc": desc}
    dic = json.dumps(dic).encode("utf-8")
    print(dic)
    return HttpResponse(dic)


# 使用ajax上传文件
@auth
def upload_img(request):
    obj = request.FILES.get("img")
    img_path = os.path.join("static", "images", obj.name)
    with open(img_path, mode="wb") as f:
        for chunk in obj.chunks():
            f.write(chunk)
    data = {
        'status': True,
        'path': img_path,
    }
    return HttpResponse(json.dumps(data))



# 使用iframe伪ajax上传文件
# @auth
# def upload_img(request):
#     response = BaseResponse()
#     try:
#         obj = request.FILES.get("img")
#         img_path = os.path.join("static", "images", obj.name)
#         with open(img_path, mode="wb") as f:
#             for chunk in obj.chunks():
#                 f.write(chunk)
#         print(123)
#     except Exception as e:
#         response.msg = str(e)
#     else:
#         response.status = True
#         response.path = img_path
#     return HttpResponse(json.dumps(response.get_dict()))


@auth
def AddNews(request):
    title = request.POST.get("title_name")
    url = request.POST.get("url_name").split("/")[2]
    summary = request.POST.get("message_text")
    avatar = request.POST.get("avatar")
    news_type = request.POST.get("news_type")
    news_id = models.NewsType.objects.filter(caption=news_type).first().id
    ctime = time.time()
    user = request.session.get("session_msg")
    user_id = models.UserInfo.objects.filter(username=user).first().id
    print(title,url,summary,avatar,news_type,news_id,ctime,user,user_id)
    models.News.objects.create(title=title, url=url, summary=summary, avatar=avatar, new_type_id=news_id, ctime=ctime, user_id=user_id)
    return redirect('/index/')

@auth
def do_like(request):
    response = LikeResponse()
    try:
        new_id = request.POST.get("newid")
        username = request.session.get("session_msg")
        id = models.UserInfo.objects.filter(username=username).first().id
        ctime = time.time()
        exist_like = models.Like.objects.filter(news_id=new_id, user_id=id).count()
        with transaction.atomic():
            if exist_like:
                models.Like.objects.filter(news_id=new_id, user_id=id).delete()
                models.News.objects.filter(id=new_id).update(like_count=F('like_count') - 1)
                response.code = 666
            else:
                models.Like.objects.create(user_id=id, news_id=new_id, ctime=ctime)
                models.News.objects.filter(id=new_id).update(like_count=F('like_count') + 1)
                response.code = 999
    except Exception as e:
        response.msg = str(e)
    else:
        response.status = True
    return HttpResponse(json.dumps(response.get_dict()))



def build_comment(data):
    dic = {}
    for item in data:
        item['children'] = []
        dic[item["id"]] = item
    result = []
    for item in data:
        pid = item['parent_id']
        if pid:
            dic[pid]["children"].append(item)
        else:
            result.append(item)
    return result


def build_comment_tree(com_list):
    tpl = """
    <div class="root">
        <div class="sons" click="Hide()">{0}：{1}</div>
        <div class="grandson">{2}</div>
    </div>
    """
    html = ""
    for item in com_list:
        if not item['children']:
            html += tpl.format(item['user__username'], item['content'], "")
        else:
            html += tpl.format(item['user__username'], item['content'], build_comment_tree(item['children']))
    return html

@auth
def comment(request):
    nid = request.POST.get("nid")
    comment = models.Comment.objects.filter(new_id=nid).values("content", "id", "user__username", "parent_id")
    result = build_comment(comment)
    html = build_comment_tree(result)
    return HttpResponse(json.dumps(html))









