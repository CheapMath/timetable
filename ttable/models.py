
from  timetable import settings
from django.db import models
from django.http import JsonResponse
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import AbstractUser
import requests
import json
from rest_framework.views import APIView

# Create your models here.


class User(AbstractUser):

    GENDER_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    ]

    # 微信登陆用参数
    gender = models.SmallIntegerField(choices=GENDER_ITEMS, default=0, verbose_name="性别")
    avatar_url = models.CharField(max_length=50, default="", null=True, blank=True, verbose_name="头像")
    openid = models.CharField(max_length=64, db_index=True, verbose_name='openid')
    nickname=models.CharField(max_length=50,verbose_name="微信名")

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'tb_users'
        verbose_name = verbose_name_plural = "用户"


class Student(models.Model):
    SEX_ITEMS=[
        (1,'男'),
        (2,'女'),
        (0,'未知'),
    ]

    STATUS_ITEMS=[
        (0,'申请'),
        (1,'通过'),
        (2,'拒绝'),
    ]

    GRADE_ITEMS=[
        (0,'小学'),
        (1,'初中'),
        (2,'高中'),
    ]

    CLASS_ITEMS=[
        (1,'一年级'),
        (2,'二年级'),
        (3,'三年级'),
        (4,'四年级'),
        (5,'五年级'),
        (6,'六年级'),
    ]

    name=models.CharField(max_length=128,verbose_name="姓名")
    sex=models.IntegerField(choices=SEX_ITEMS,verbose_name="性别")
    grades=models.IntegerField(choices=GRADE_ITEMS,verbose_name="年级")
    classes=models.IntegerField(choices=CLASS_ITEMS,verbose_name="班级")
    birth=models.DateField(auto_now=False,editable=True,verbose_name="出生日期")
    status=models.IntegerField(choices=STATUS_ITEMS,default=0,verbose_name="审核状态")
    created_time=models.DateTimeField(auto_now=True,editable=False,verbose_name="创建时间")
    created_user=models.CharField(max_length=128,verbose_name="创建者openid")

    #创建两类账户的关联表
    user = models.ManyToManyField(User, through='Student_USER')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "学生"




    #使用这种方法后只有通过该类的实例化来修改数据库；
class Student_USER(models.Model):
    Relation_Type = [
        (0,'创建者'),
        (1,'被邀请者'),
    ]
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relation_type = models.IntegerField(choices=Relation_Type,verbose_name="关系类型")


    class Meta:
        verbose_name = verbose_name_plural = "学生—用户关系组"




class WechatLoginView(APIView):
    """
    微信登录逻辑
    """
    def WXLogin(self, request):

        # 前端发送code到后端,后端发送网络请求到微信服务器换取openid
        code = request.data.get('code')
        if not code:
            #return Response({'message': '缺少code'}, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({'message': '缺少code'}, status=400)

        '''
        登录凭证校验。通过 wx.login 接口获得临时登录凭证 code 后传到开发者服务器调用此接口完成登录流程。
        说明页面：https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/login/auth.code2Session.html
        '''
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
            .format(settings.APP_ID, settings.APP_SECRET, code)
        r = requests.get(url)
        res = json.loads(r.text)
        openid = res['openid'] if 'openid' in res else None
        # session_key = res['session_key'] if 'session_key' in res else None
        if not openid:
            return JsonResponse({'message': '微信调用失败'}, status=503)

        # 判断用户是否第一次登录
        try:
            user = User.objects.get(openid=openid)
        except Exception:
            # 微信用户第一次登陆,新建用户
            username = request.data.get('openid')
            nickname=request.data.get('nickname')
            avatar_url = request.data.get('avatar_url')
            #性别
            gender = request.data.get('gender')
            #创建过程
            user = User.objects.create(username=username, nickname=nickname, avatar_url=avatar_url,gender=gender)
            user.set_password(openid)

        # 手动签发jwt-TOKEN,小程序客户端收到后保存到local storage，每次接口调用都需要带上，服务器端需要
        '''
        jwt_payload_handler 专门对payload加密
        jwt_encode_handler方法对三个部分加密生成token
        '''
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        #？？待新增返回绑定的student信息

        #dict类型
        resp_data = {
            "status": 'success',
            "nickname": user.username,
            "avatar_url":avatar_url,
            "user_id": user.id,
            "token": token,
        }
        # JsonResponse 将dict转换成json返回给客户端
        return JsonResponse(resp_data)

















