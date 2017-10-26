from django.shortcuts import render,redirect
from django.forms.models import model_to_dict
from book.models import *
# Create your views here.1

def index(request):
    all_author_list = Author.objects.all()
    all_publish_list = Publish.objects.all()
    book_list = Book.objects.all()
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
        author_id = book.author_id
        author = Author.objects.get(id=author_id).name
        publish_id = book.publish_id
        publish = Publish.objects.get(id=publish_id).name
        book_dic["author"] = author
        book_dic["publish"] = publish
        all_book_list.append(book_dic)
    return render(request,"login.html",locals())


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
        author = request.POST.get("author")
        # author = request.POST.getlist("author") 获取多选框的多个值
        publish = request.POST.get("publish")
        info = request.POST.get("info")
        # 添加数据库
        aut = Author.objects.get(name=author)
        pub = Publish.objects.get(name=publish)
        Book.objects.create(title=title, price=price, author=aut, publish=pub, info=info)
        return redirect("/index/")
    return render(request, "addHosts.html" ,locals())

def BookInfo(request):
    id = request.GET.get("id")
    bookinfo = Book.objects.filter(id=id)[0]
    return render(request, "HostInfo.html", locals())


def ediBook(request):
    title = request.POST.get("title")
    price = request.POST.get("price")
    info = request.POST.get("info")
    author = request.POST.get("author")
    publish = request.POST.get("publish")
    author_id = Author.objects.get(name=author).id
    print(author_id)
    publish_id = Publish.objects.get(name=publish).id
    print(publish_id)
    ID = request.POST.get("ID")
    Book.objects.filter(id=ID).update(title=title, price=price, author_id=author_id, publish_id=publish_id, info=info)
    return redirect("/index/")