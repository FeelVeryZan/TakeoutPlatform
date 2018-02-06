from django.db import models

# 把一坨东西转化为字符串，强行回避所有异常
def toStringWithoutError(obj):
    try:
        return str(obj)
    except Exception as e:
        return str(e)

# 把一坨东西转化为数字，强行回避所有异常
def toIntegerWithoutError(obj):
    try:
        return int(obj)
    except Exception as e:
        return 0

# 把UTC时间转化为本地时间，否则很尴尬
def utcToLocal(utctime):
    import time
    from datetime import datetime
    return utctime + (datetime.fromtimestamp(time.time()) - datetime.utcfromtimestamp(time.time()))

# 用户的信息
class Users(models.Model):
    # 用户在数据库中的编号
    id = models.IntegerField(primary_key=True)
    # TODO 用户在微信中的基本信息
    wxOpenId = models.TextField(max_length=256, default='')
    wxNickName = models.TextField(max_length=256, default='')
    WX_SEX_CHOICE = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )
    wxSex = models.IntegerField(choices=WX_SEX_CHOICE, default=0)
    # 首次登陆时间
    signUpTime = models.DateTimeField(auto_now_add=True)
    # 上次登陆时间
    lastLoginTime = models.DateTimeField(auto_now=True)
    # 收到的站内消息数量
    messageCount = models.IntegerField(default=0)
    # 身份信息
    IDENTITY_CHOICES = (
        (0, '普通用户'),
        (1, '店铺老板'),
        (2, '管理员'),
    )
    identity = models.IntegerField(choices=IDENTITY_CHOICES, default=0)
    # 如果是管理员，就记录管理员密码，否则是None
    passwordOfAdministrator = models.TextField(null=True, default=None)
    # 如果是店铺老板，就记录自己的店铺的编号，否则是None
    isTheOwnerOfWhich = models.IntegerField(null=True, default=None)
    # 收货地址和联系方式的数量
    addressCount = models.IntegerField(default=0)
    # 收货地址和联系方式的列表，以 "姓名|电话|地址#姓名|电话|地址#...#姓名|电话|地址"的形式存储
    addressListStr = models.TextField(max_length=65536, default='')
    # 获取地址列表，[[姓名, 电话, 地址], ...]
    def getAddressList(self):
        addressStrList = self.addressListStr.split('#')
        addressList = []
        for addressStr in addressStrList:
            addressList.append(addressStr.split('|'))
        return addressList
    # 调试输出
    def __str__(self):
        return 'User.models.Users(' + ', '.join([
            'id=' + toStringWithoutError(self.id),
            'wxOpenId=' + toStringWithoutError(self.wxNickName),
            'wxNickName=' + toStringWithoutError(self.wxNickName),
            'wxSex=' + toStringWithoutError(self.wxSex),
            'signUpTime=' + toStringWithoutError(utcToLocal(self.signUpTime).strftime("%Y-%m-%d %H:%M:%S")),
            'lastLoginTime=' + toStringWithoutError(utcToLocal(self.lastLoginTime).strftime("%Y-%m-%d %H:%M:%S")),
            'messageCount=' + toStringWithoutError(self.messageCount),
            'identity=' + toStringWithoutError(self.identity),
            'passwordOfAdministrator=' + toStringWithoutError(self.passwordOfAdministrator),
            'isTheOwnerOfWhich=' + toStringWithoutError(self.isTheOwnerOfWhich),
            'addressCount=' + toStringWithoutError(self.addressCount),
            'addressListStr=' + toStringWithoutError(self.addressListStr),
        ]) + ')'


# 每条用户收藏店铺记录的信息
class CollectS(models.Model):
    # 这条记录在数据库中的编号
    id = models.IntegerField(primary_key=True)
    # 用户的编号
    userId = models.IntegerField()
    # 店铺的编号
    shopId = models.IntegerField()
    # 这条记录添加的时间
    addTime = models.DateTimeField()
    # 调试输出
    def __str__(self):
        return 'User.models.CollectS(' + ', '.join([
            'id=' + toStringWithoutError(self.id),
            'userId=' + toStringWithoutError(self.userId),
            'shopId=' + toStringWithoutError(self.shopId),
            'addTime=' + toStringWithoutError(utcToLocal(self.addTime).strftime("%Y-%m-%d %H:%M:%S")),
        ]) + ','


# 每条用户收藏商品记录的信息
class CollectG(models.Model):
    # 这条记录在数据库中的编号
    id = models.IntegerField(primary_key=True)
    # 用户的编号
    userId = models.IntegerField()
    # 商品的编号
    goodsId = models.IntegerField()
    # 这条记录添加的时间
    addTime = models.DateTimeField()
    # 调试输出
    def __str__(self):
        return 'User.models.CollectG(' + ', '.join([
            'id=' + toStringWithoutError(self.id),
            'userId=' + toStringWithoutError(self.userId),
            'goodsId=' + toStringWithoutError(self.goodsId),
            'addTime=' + toStringWithoutError(utcToLocal(self.addTime).strftime("%Y-%m-%d %H:%M:%S")),
        ]) + ')'


# 每个用户订单的信息
class Orders(models.Model):
    # 这条记录在数据库中的编号
    id = models.IntegerField(primary_key=True)
    # 用户的编号
    userId = models.IntegerField()
    # 订单使用用户的哪一个收货地址
    userAddressId = models.IntegerField(default=0)
    # 店铺的编号
    shopId = models.IntegerField()
    # 订单中的商品种类数量
    goodsCount = models.IntegerField(default=0)
    # 订单中商品的编号和数量的列表，用 "编号|数量#编号|数量#...#编号|数量" 的形式存储
    goodsListStr = models.TextField(max_length=65536, default='')
    # 下单时间
    addTime = models.DateTimeField(auto_now_add=True)
    # 订单的状态
    STATE_CHOICE = (
        (0, '下单后配送中'),
        (1, '用户取消'),
        (2, '商家取消'),
        (3, '已完成待评论'),
        (4, '已评论'),
    )
    state = models.IntegerField(choices=STATE_CHOICE, default=0)
    # 如果已评论，就要存评论的分数
    feedbackScore = models.IntegerField(null=True, default=None)
    # 如果已评论，就要存评论的文字内容
    feedbackContent = models.TextField(max_length=65536, default=None)
    # 获取订单中的商品和数量列表，[[商品]]
    def getGoodsList(self):
        goodsStrList = self.goodsListStr.split('#')
        goodsList = []
        for goodsStr in goodsStrList:
            goods = goodsStr.split('|')
            goodsList.append(int(goods[0], int(goods[1])))
        return goodsList
    def __str__(self):
        return 'User.models.Orders)' + ', '.join([
            'id=' + toStringWithoutError(self.id),
            'userId=' + toStringWithoutError(self.userId),
            'userAddressId=' + toStringWithoutError(self.userAddressId),
            'shopId=' + toStringWithoutError(self.shopId),
            'goodsListStr=' + toStringWithoutError(self.goodsListStr),
            'addTime=' + toStringWithoutError(utcToLocal(self.addTime).strftime("%Y-%m-%d %H:%M:%S")),
            'state=' + toStringWithoutError(self.state),
            'feedbackScore=' + toStringWithoutError(self.feedbackScore),
            'feedbackContent=' + toStringWithoutError(self.feedbackContent),
        ]) + ')'

