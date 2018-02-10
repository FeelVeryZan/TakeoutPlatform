# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

from Shop.models import Shops, Goods
from User.models import Users, CollectG, CollectS, Orders

# 渲染登录页面
def visitLoginPage(request):
    print('    visitLoginPage')
    msgMap = {}
    userName = request.GET.get('userName', None)
    password = request.GET.get('password', None)
    if userName is None or password is None:
        # 刚打开登陆页面，还没有输入用户名和密码
        msgMap['userName'] = ''
        msgMap['firstVisitLoginPage'] = True
        return render(request, 'LoginPage.html', msgMap)
    # 是从登陆页面发出的登陆请求
    userList = Users.objects.filter(wxOpenId=userName)
    if len(userList) != 1 or \
        userList[0].passwordOfAdministrator != password or \
        userList[0].identity != 2:
        # 登陆失败
        msgMap['userName'] = userName
        msgMap['firstVisitLoginPage'] = False
        return render(request, 'LoginPage.html', msgMap)
    # 登陆成功
    request.session['userId'] = userList[0].id
    request.session['userName'] = userList[0].wxOpenId
    request.session['identity'] = userList[0].identity
    print('session = ', dict(request.session))
    return HttpResponseRedirect('/home/')

# 渲染网站主页
def visitHomePage(request):
    print('    visitHomePage')
    print('session = ', dict(request.session))
    if request.session.get('userId', None) == None:
        return HttpResponseRedirect('/')
    msgMap = {}
    return render(request, 'HomePage.html', msgMap)

# 渲染“找不到页面”的页面
def visitNotFoundPage(request):
    return render(request, 'PageNotFound.html')

# 渲染搜索页面
def visitSearchPage(request):
    print('    visitSearchPage')
    msgMap = {}
    return render(request, 'SearchPage.html', msgMap)

# 渲染搜索结果，静态刷新搜索页面
def visitSearchStaticRefresh(request):
    print('    visitSearchStaticRefresh')
    text = request.GET.get('text', None)
    msgMap = {}
    shopList = list(Shops.objects.all()[:10])
    msgMap['shopList'] = shopList
    return render(request, 'SearchStaticRefresh.html', msgMap)
