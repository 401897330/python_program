from django.shortcuts import render,HttpResponse,redirect
import time,re
import requests,json
from utils.ticket import get_ticket_dict


def ticket(html):
    from bs4 import BeautifulSoup
    ret = {}
    soup = BeautifulSoup(html,"html.parser")
    for tag in soup.find(name='error').find_all():
        ret[tag.name] = tag.text
    return ret


def login(req):
    if req.method == "GET":
        uuid_time = int(time.time()*1000)
        base_uuid_url = "https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zhCN&={0}"
        uuid_url = base_uuid_url.format(uuid_time)
        rl = requests.get(uuid_url)
        uuid = re.findall('= "(.*)";', rl.text)[0]
        req.session["UUID"] = uuid
        return render(req, "login.html",locals())



def check_login(req):
    response = {'code':408,'data':None}
    ctime = int(time.time()*1000)
    base_login_url = "https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=0&r=-691927576&_={1}"
    login_url = base_login_url.format(req.session['UUID'], ctime)
    rl = requests.get(login_url)
    if "window.code=408" in rl.text:
        response['code'] = 408
    elif "window.code=201" in rl.text:
        response['code'] = 201
        response['data'] = re.findall("window.userAvatar = '(.*)';", rl.text)
    elif "window.code=200" in rl.text:
        print("确认登陆", rl.text)
        req.session["LOGIN_COOKIE"] = rl.cookies.get_dict()
        base_redircute_rul = re.findall('redirect_uri="(.*)";', rl.text)[0]
        redirect_url = base_redircute_rul + "&fun=new&version=v2&lang=zh_CN"

        #获取凭证
        r2 = requests.get(redirect_url)
        ticket_dict = get_ticket_dict(r2.text)
        req.session['TICKET_DICT'] = ticket_dict
        print(r2.cookies.get_dict())
        req.session['TICKET_COOKIE'] = r2.cookies.get_dict()
        print('获取到凭证', ticket_dict)
        response['code'] = 200
    return HttpResponse(json.dumps(response))



def index(request):
    # 初始化获取最近联系人信息
    ticket_dict = request.session['TICKET_DICT']
    post_data = {
        "BaseRequest": {
            "DeviceID": "e858922995478418",
            "Sid": ticket_dict["wxsid"],
            "Skey": ticket_dict["skey"],
            "Uin": ticket_dict["wxuin"],
        }
    }
    init_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-871332085&lang=zh_CN&pass_ticket={0}".format(ticket_dict['pass_ticket'])
    r3 = requests.post(init_url, data=json.dumps(post_data), headers={'Content-Type':'application/json;charset=utf-8'})
    r3.encoding = "utf-8"
    init_dict = json.loads(r3.text)

    sync_key = init_dict.pop('SyncKey')

    request.session['sync_key'] = sync_key
    request.session['init_dict'] = init_dict
    request.session['init_cookie_dict'] = r3.cookies.get_dict()
    return render(request, 'index.html', locals())


def avatar(request):
    print('开始获取头像')
    base_url = "https://wx.qq.com"
    k = request.GET.get('k')
    username = request.GET.get('username')
    skey = request.GET.get('skey')

    avatar_url = "{0}{1}&username={2}&skey={3}".format(base_url, k, username, skey)
    print(avatar_url)
    all_cookies = {}
    all_cookies.update(request.session['LOGIN_COOKIE'])
    all_cookies.update(request.session['TICKET_COOKIE'])
    all_cookies.update(request.session['init_cookie_dict'])
    response = requests.get(avatar_url,
                            headers={
                                'Referer': 'https://wx.qq.com/?&lang=zh_CN',
                                'Host': 'wx.qq.com',
                                'Content-Type': 'image/jpeg',
                                'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
                                'Accept': "image/webp,image/apng,image/*,*/*;q=0.8",
                            }, cookies=all_cookies)
    return HttpResponse(response.content)
