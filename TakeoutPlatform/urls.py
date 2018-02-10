"""TakeoutPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import Home.views as Home_views
import Shop.views as Shop_views
import User.views as User_views
import Manager.views as Manager_views

urlpatterns = [
    # 访问登陆页面
    path('', Home_views.visitLoginPage),
    # 从登陆页面返回
    path('login/', Home_views.visitLoginPage),
    # 访问“找不到页面”的页面
    path('notFound/', Home_views.visitNotFoundPage),
    # 访问网站主页
    path('home/', Home_views.visitHomePage),
    # 访问搜索页面
    path('search/', Home_views.visitSearchPage),
    # 静态刷新搜索页面
    path('search/static_refresh/', Home_views.visitSearchStaticRefresh),
    # 访问店铺页面
    path('shop/<int:shopId>/', Shop_views.visitShopPage),
    # 访问管理员主页
    path('manage/', Manager_views.visitManagePage),
    # 访问手动添加新商家的页面
    path('manage/addNewShop/', Manager_views.visitAddNewShop),
    # 访问处理投诉的页面
    path('manage/handlingComplaint/', Manager_views.visitHandlingComplaint),
    # 访问审核店铺变动
    path('manage/examineAndVerify/', Manager_views.visitExamineAndVerify),

    # Django自带的页面，应该是可以删掉的吧
    path('admin/', admin.site.urls),
]
