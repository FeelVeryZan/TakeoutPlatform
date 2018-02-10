from django.shortcuts import render

from Shop.models import Shops, Goods
from User.models import toIntegerWithoutError

# 渲染店铺页面
def visitShopPage(request, shopId):
    print('    visitShopPage')
    msgMap = {}
    if shopId is None:
        return render(request, 'PageNotFound.html')
    if type(shopId) is not int:
        shopId = toIntegerWithoutError(shopId)
    shopList = Shops.objects.filter(id=shopId)
    if len(shopList) != 1:
        return render(request, 'PageNotFound.html')
    msgMap['shopObj'] = shopList[0]
    goodsList = Goods.objects.filter(shopId=shopId)
    msgMap['goodsList'] = goodsList
    msgMap['goodsCnt'] = len(goodsList)
    return render(request, 'ShopPage.html', msgMap)
