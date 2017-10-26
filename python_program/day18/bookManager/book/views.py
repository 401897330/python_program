from django.shortcuts import render,redirect,HttpResponse
from django.forms.models import model_to_dict
from book.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.1

def index(request):
    try:
        all_author_list = Author.objects.all()
        all_publish_list = Publish.objects.all()
        book_list = Book.objects.all()
        order_number = 0
        if request.method == "POST":
            keyword = request.POST.get("keyword")
            book_list = Book.objects.filter(title__contains=keyword)
        all_book_list = []
        for book in book_list:
            book_dic = {}
            book_dic["id"] = book.id
            book_dic["title"] = book.title
            book_dic["price"] = book.price
            book_dic["info"] = book.info
            author_queryset = Book.objects.filter(id=book.id).values("author__name")
            author_list = []
            for author in author_queryset:
                author_list.append(author["author__name"])
            author = ",".join(author_list)
            publish_queryset = Book.objects.filter(id=book.id).values("publish__name")
            publish = publish_queryset[0]["publish__name"]
            book_dic["author"] = author
            book_dic["publish"] = publish
            all_book_list.append(book_dic)

        p = Paginator(all_book_list, 6)
        page = request.GET.get("page")
        page_num = range(1,11)
        if page:
            num1 = int(page) - 7
            page_num2 = range(num1, int(page)+1)
            page = int(page)
            if int(page) >= p.num_pages:
                all_book_list = p.page(p.num_pages)
            else:
                all_book_list = p.page(int(page))
        else:
            all_book_list = p.page(1)
        return render(request, "login.html", locals())
    except EmptyPage:
        all_book_list = all_book_list = p.page(1)
        return render(request, "login.html", locals())



def delBook(request):
    id = request.GET.get("id")
    Book.objects.filter(id=id).delete()
    return redirect("/index/")


def addBook(request):
    all_author_list = Author.objects.all()
    all_publish_list = Publish.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        author = request.POST.getlist("author") #获取多选框的多个值
        publish = request.POST.get("publish")
        info = request.POST.get("info")
        # 添加数据库
        pub_id = Publish.objects.get(name=publish).id
        Book.objects.create(title=title, price=price, publish_id=pub_id, info=info)
        book_id = Book.objects.all().last().id
        book_obj = Book.objects.get(id=book_id)
        for name in author:
            author = Author.objects.get(name=name)
            book_obj.author.add(author)

    return render(request, "addHosts.html" ,locals())

def BookInfo(request):
    id = request.GET.get("id")
    bookinfo = Book.objects.filter(id=id)[0]
    return render(request, "HostInfo.html", locals())


def ediBook(request):
    title = request.POST.get("title")
    price = request.POST.get("price")
    info = request.POST.get("info")
    author = request.POST.getlist("author")
    publish = request.POST.get("publish")
    publish_id = Publish.objects.get(name=publish).id
    ID = request.POST.get("ID")
    Book.objects.filter(id=ID).update(title=title, price=price, publish_id=publish_id, info=info)
    book_obj = Book.objects.get(id=ID)
    book_obj.author.clear()
    for name in author:
        author = Author.objects.get(name=name)
        book_obj.author.add(author)
    return redirect("/index/")

def add(request):
    # 批量导入book_book_author数据
    # import random
    # for i in range(2,102):
    #     book_obj = Book.objects.get(id=i)
    #     num = random.randrange(1,4)
    #     author_list = Author.objects.filter(id=num)
    #     book_obj.author.add(*author_list)

    # 批量导入book_book数据
    Booklist = []
    # for i in range(100):
    #     Booklist.append(Book(title="book" + str(i), price=30 + i * i, publish_id="3", info="hello world"))
    # Book.objects.bulk_create(Booklist)
    return HttpResponse("OK")


def login(request):
    return render(request,"login.html")


def register(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_pwd = request.POST.get("user_pwd")
        re_user_pwd = request.POST.get("re_user_pwd")
        e_mail = request.POST.get("re_user_pwd")
        if user_pwd != re_user_pwd:
            pass
        else:
            pass
    return render(request,"register.html",locals())