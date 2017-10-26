from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class NewsType(models.Model):
    caption = models.CharField(max_length=16)

class News(models.Model):
    title = models.CharField(verbose_name="标题",max_length=32)
    url = models.CharField(verbose_name="URL",max_length=1024)
    avatar = models.CharField(verbose_name="头像",max_length=1024)
    summary = models.CharField(verbose_name="简介",max_length=1024)
    new_type = models.ForeignKey(verbose_name="新闻类型", to="NewsType")
    user = models.ForeignKey(verbose_name="发布者", to="UserInfo")
    ctime = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)


class Comment(models.Model):
    content = models.CharField(verbose_name="评论内容", max_length=255)
    new = models.ForeignKey(verbose_name="评论者", to="News")
    user = models.ForeignKey(verbose_name="简介", to="UserInfo")
    ctime = models.DateTimeField(verbose_name="评论时间",auto_now_add=True)
    parent = models.ForeignKey('Comment',related_name="par",null=True,blank=True)


class Like(models.Model):
    user = models.ForeignKey(to="UserInfo")
    news = models.ForeignKey(to="News")
    ctime = models.DateTimeField(verbose_name="点赞时间",auto_now_add=True)
    #Meta这个类的作用是限制多对多的字段重复。
    class Meta:
        unique_together = [
            ("user", "news")
        ]