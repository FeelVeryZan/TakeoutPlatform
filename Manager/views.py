from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# 渲染管理员主页
def visitManagePage(request):
    print('    visitManagePage')
    if request.session.get('identity', -1) != 2:
        return HttpResponseRedirect('/')
    return render(request, 'ManagePage.html')

# 渲染手动添加新商家的页面
def visitAddNewShop(request):
    print('    visitAddNewShop')
    if request.session.get('identity', -1) != 2:
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/notFound/')

# 渲染处理投诉的页面
def visitHandlingComplaint(request):
    print('    visitHandlingComplaint')
    if request.session.get('identity', -1) != 2:
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/notFound/')

# 渲染审核店铺变动的页面
def visitExamineAndVerify(request):
    print('    visitExamineAndVerify')
    if request.session.get('identity', -1) != 2:
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/notFound/')

