from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from user.forms import RegisterForm
from user.models import User


def register(request):
   if request.method == 'POST':
       form = RegisterForm(request.POST, request.FILES)
       print('ss')
       if form.is_valid():
           # form表单可以直接将icon等保存到数据库　
           # commit = False 先拿到资料　Ｔrue保存到数据库
           user = form.save(commit=False)
           user.password = make_password(user.password)
           user.save()

           # 设置用户登录状态
           request.session['uid'] = user.id
           request.session['nickname'] = user.nickname
           request.session['icon'] = user.icon.url

           return redirect('/user/info/')
       else:
           return render(request,'register.html',{'error':form.errors})
   return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        # nickname = request.POST.get('nickname')
        # users = User.objects.filter(nickname=nickname)
        # if users.exists():
        #     user = users.first()
        #     password = request.POST.get('password')
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')

        try:
            user = User.objects.get(nickname=nickname)
        except User.DoesNotExist:
            return render(request, 'login.html',
                          {'error': '用户不存在', })
        if check_password(password,user.password):
                request.session['uid'] = user.id
                request.session['nickname'] = user.nickname
                request.session['icon'] = user.icon.url
                return redirect('/user/info/')


    return render(request,'login.html')


def logout(request):
    request.session.flush()
    return redirect('/post/list/')


def user_info(request):
    uid = request.session.get('uid')
    user = User.objects.get(id=uid)
    return render(request,'user_info.html',{'user':user})