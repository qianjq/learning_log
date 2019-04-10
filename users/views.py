from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
	"""注销用户"""
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """注册新用户"""
    # 如果不是 POST 请求，就先创建一个 UserCreationForm实例
    # UserCreationForm：默认表单
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            # 如果提交的数据有效，我们调用表单的 save()，将用户名和密码的散列值保存到数据库。
            # 方法 save() 返回新创建的用户对象，我们将其存储到 new_user 中。
            new_user = form.save()

            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)