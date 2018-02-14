# -*- coding: utf-8 -*-

import os
import django
from subprocess import Popen

try:
    os.remove('db.sqlite3')
except Exception as e:
    print(e)

Popen('python manage.py makemigrations', shell=True).wait()
Popen('python manage.py migrate --run-syncdb', shell=True).wait()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TakeoutPlatform.settings")
django.setup()

import django.utils.timezone as timezone
import datetime
import hashlib

from Shop.models import Shops, Goods
from User.models import Users, CollectS, CollectG, Orders

# 添加管理员用户
userAdmin = Users.objects.create(
    id=1,
    wxOpenId='admin',
    identity=2,
    passwordOfAdministrator=hashlib.sha512('123456'.encode('utf-8')).hexdigest(),
)

# 添加一个样例店铺，有两个老板
Shops.objects.create(
    id=1,
    name='沙县小吃(sample)',
    description='沙县小吃，就是好吃，不信你就赶紧来吃！',
    logo='/static/images/shop/1-沙县小吃(sample).png',
    address='重庆江北区红砂碛26号附99号',
    phoneNumber='13206188085,15111811885',
    ownerCnt=2,
    ownerListStr='2|3',
)
Users.objects.create(
    id=2,
    identity=1,
    isTheOwnerOfWhich=1,
)
Users.objects.create(
    id=3,
    identity=1,
    isTheOwnerOfWhich=1,
)

# 添加商品


# 添加一个样例店铺，有一个老板
Shops.objects.create(
    id=2,
    name='黔江古镇鸡杂(sample)',
    description='鸡杂有大锅小锅之分，汤底较厚，味道很鲜，还有点回甜。朋友聚餐、情侣约会、休闲时光、随便吃吃、随便吃吃、朋友聚餐、情侣约会、休闲时光、随便吃吃。提供在线菜单,提供在线菜单。营业时间：10:00-22:30',
    logo='/static/images/shop/2-黔江古镇鸡杂(sample).png',
    address='重庆沙坪坝区小龙坎正街290号附17号',
    phoneNumber='(023)65308835',
    ownerCnt=1,
    ownerListStr='4'
)
Users.objects.create(
    id=4,
    identity=1,
    isTheOwnerOfWhich=2,
)

# 添加商品





