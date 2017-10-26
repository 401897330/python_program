from django.shortcuts import render,redirect
from book.models import *
# Create your views here.
def index(request):
    all_book_list = Book.objects.all()
    if request.method=="POST":
        keyword = request.POST.get("keyword")
        all_book_list = Book.objects.filter(title__contains=keyword)
    return render(request,"login.html",{"all_book_list":all_book_list})

def addBook(request):
    if request.method=="POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        author = request.POST.get("author")
        publish = request.POST.get("publish")
        info = request.POST.get("info")
        # 添加数据库
        Book.objects.create(title=title, price=price, author=author, publiosh=publish, info=info)
        return redirect("/index/")
    return render(request, "addHosts.html")

def delBook(request):
    id = request.GET.get("id")
    Book.objects.filter(id=id).delete()
    return redirect("/index/")

def ediBook(request):
    title = request.POST.get("title")
    price = request.POST.get("price")
    author = request.POST.get("author")
    publish = request.POST.get("publiosh")
    info = request.POST.get("info")
    ID = request.POST.get("ID")
    print(ID)
    Book.objects.filter(id=ID).update(title=title, price=price, author=author, publiosh=publish, info=info)
    return redirect("/index/")

def BookInfo(request):
    id = request.GET.get("id")
    bookinfo = Book.objects.filter(id=id)[0]
    print(id)
    return render(request, "HostInfo.html", {"bookinfo": bookinfo})





