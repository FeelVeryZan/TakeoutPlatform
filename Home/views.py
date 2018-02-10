# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render

from Shop.models import Shops, Goods
from User.models import Users, CollectG, CollectS, Orders

# 渲染网站主页
def visitHomepage(request):
    print('    visitHomepage')
    msgMap = {}
    return render(request, 'Homepage.html', msgMap)

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
