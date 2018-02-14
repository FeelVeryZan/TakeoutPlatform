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
    if userList[0].identity == 2:
        return HttpResponseRedirect('/manage/')
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
    if request.session.get('userId', None) == None:
        return HttpResponseRedirect('/')
    msgMap = {}
    sortMethodList = ['综合排序', '好评优先', '起送价最低', '配送最快']
    msgMap['sortMethodList'] = sortMethodList
    filterSellerList = ['蜂鸟专送', '准时达', '平拍商家', '外卖保', '新店', '开发票', '接受预定', '会员领红包']
    msgMap['filterSellerList'] = filterSellerList
    filterDiscountList = ['新用户优惠', '特价商品', '下单立减', '赠品优惠', '下单返红包', '进店领红包']
    msgMap['filterDiscountList'] = filterDiscountList
    msgMap['shopList'] = []
    return render(request, 'SearchPage.html', msgMap)

# 渲染搜索结果，静态刷新搜索页面
def visitSearchStaticRefresh(request):
    print('    visitSearchStaticRefresh')
    if request.session.get('userId', None) == None:
        return HttpResponseRedirect('/')
    text = request.GET.get('text', None)
    msgMap = {}
    shopList = list(Shops.objects.all()[:10])
    for shop in shopList:
        if len(shop.description) < 50:
            shop.descWithLimit = shop.description
        else:
            shop.descWithLimit = shop.description[:47] + "..."
    msgMap['shopList'] = shopList
    return render(request, 'SearchStaticRefresh.html', msgMap)
