# coding: utf-8
from django.db import models

from User.models import toStringWithoutError
from User.models import toIntegerWithoutError
from User.models import utcToLocal

# 店铺的信息
class Shops(models.Model):
    # 店铺的在数据库中的编号
    id = models.IntegerField(primary_key=True)
    # 店铺的名称
    name = models.CharField(max_length=256, default='暂无名称')
    # 店铺的简介
    description = models.CharField(max_length=65536, default='暂无简介')
    # 店铺的图标
    logo = models.ImageField(upload_to='Shop/images/ShopsLogo/', default='Shop/images/ShopsLogo/None.png')
    # 店铺的地址
    address = models.TextField(max_length=256, default='暂无地址')
    # 店铺的电话，多个号码用逗号隔开
    phoneNumber = models.TextField(max_length=256, default='暂无电话')
    # 店铺的老板数量
    ownerCnt = models.IntegerField()
    # 店铺老板（们）的用户编号，用 "编号|编号|...|编号" 的形式存储
    ownerListStr = models.TextField(max_length=256, default='')
    # 店铺注册的时间
    signUpTime = models.DateTimeField(auto_now_add=True)
    # 店铺的商品数量
    goodsCount = models.IntegerField(default=0)
    # 店铺的总销售量
    totalSales = models.IntegerField(default=0)
    # 店铺的月销售量
    monthlySales = models.IntegerField(default=0)
    # 店铺的周销售量
    weeklySales = models.IntegerField(default=0)
    # 店铺的日销售量
    dailySales = models.IntegerField(default=0)
    # 获取老板编号列表，[编号,编号,...]
    def getOwnerList(self):
        ownerStrList = self.ownerListStr.split('|')
        ownerList = []
        for ownerStr in ownerStrList:
            ownerList.append(int(ownerStr))
        return ownerList
    # 调试输出
    def __str__(self):
        return 'Shop.models.Shops(' + ', '.join([
            'id=' + toStringWithoutError(self.id),
            'name=' + toStringWithoutError(self.name),
            'description=' + toStringWithoutError(self.description),
            'logo=' + toStringWithoutError(self.logo),
            'address=' + toStringWithoutError(self.address),
            'phoneNumber=' + toStringWithoutError(self.phoneNumber),
            'ownerCnt=' + toStringWithoutError(self.ownerCnt),
            'ownerListStr=' + toStringWithoutError(self.ownerListStr),
            'signUpTime=' + toStringWithoutError(utcToLocal(self.signUpTime).strftime("%Y-%m-%d %H:%M:%S")),
            'goodsCount=' + toStringWithoutError(self.goodsCount),
            'totalSales=' + toStringWithoutError(self.totalSales),
            'monthlySales=' + toStringWithoutError(self.monthlySales),
            'weeklySales=' + toStringWithoutError(self.weeklySales),
            'dailySales=' + toStringWithoutError(self.dailySales),
        ]) + ')'


# 商品的信息
class Goods(models.Model):
    # 商品在数据库中的编号
    id = models.IntegerField(primary_key=True)
    # 商品的名称
    name = models.CharField(max_length=256, default='暂无名称')
    # 商品的简介
    description = models.CharField(max_length=65536, default='暂无简介')
    # 商品的样例图片
    picture = models.ImageField(null=True, default=None)
    # 商品所属的店铺编号
    shopId = models.IntegerField()
    # 商品添加的时间
    addTime = models.DateTimeField(auto_now_add=True)
    # 商品的评分次数
    scoreCnt = models.FloatField(default=0)
    # 商品的评分总和
    scoreSum = models.IntegerField(default=0)
    # 商品的总销售量
    totalSales = models.IntegerField(default=0)
    # 商品的月销售量
    monthlySales = models.IntegerField(default=0)
    # 商品的周销售量
    weeklySales = models.IntegerField(default=0)
    # 商品的日销售量
    dailySales = models.IntegerField(default=0)
    # 计算平均评分
    def getAverageScore(self):
        if self.scoreCnt == 0:
            return 0
        else:
            return float(self.scoreSum) / self.scoreCnt
    # 调试输出
    def __str__(self):
        return 'Shop.models.Goods(' + ', '.join([
            'id=' + toStringWithoutError(self.id),
            'name=' + toStringWithoutError(self.name),
            'description=' + toStringWithoutError(self.description),
            'picture=' + toStringWithoutError(self.picture),
            'shopId=' + toStringWithoutError(self.shopId),
            'addTime=' + toStringWithoutError(utcToLocal(self.addTime).strftime("%Y-%m-%d %H:%M:%S")),
            'scoreCnt=' + toStringWithoutError(self.scoreCnt),
            'scoreSum=' + toStringWithoutError(self.scoreSum),
            'totalSales=' + toStringWithoutError(self.totalSales),
            'monthlySales=' + toStringWithoutError(self.monthlySales),
            'weeklySales=' + toStringWithoutError(self.weeklySales),
            'dailySales=' + toStringWithoutError(self.dailySales),
        ]) + ')'

