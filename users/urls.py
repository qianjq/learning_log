"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面
    #url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    url( 'login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    #注册页面
    url( r'^register/$',views.register,name='register'),
    # 注销页面
    url( r'^logout/$',views.logout_view,name='logout'),
]