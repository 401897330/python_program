"""bookManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Hosts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.IndexView.as_view()),
    url(r'^addHosts/', views.addHosts),
    url(r'^delHosts/', views.delHosts),
    url(r'^ediHosts/', views.ediHosts),
    url(r'^HostInfo/', views.HostInfo),
    url(r'^add/', views.add),
    url(r'^addService/', views.addService),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^logout/', views.logout),
    url(r'^register/', views.RegisterView.as_view()),
    url(r'^manager_user/', views.ManagerUser.as_view()),
    url(r'^delUser/', views.delUser),
    url(r'^ediUser/', views.ediUser),
    url(r'^manager_service/', views.ManagerService.as_view()),
    url(r'^delService/', views.delService),
]
