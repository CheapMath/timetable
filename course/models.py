from django.db import models
from ttable.models import User
# Create your models here.

#课程标签，一种为课程包标签，一种为单节课程标签
class LABEL(models.Model):
    TYPE = [
        (0, '课程包标签'),
        (1, '单节课程标签'),
    ]
    STATUS=[
        (0,'已删除'),
        (1,'生效中'),
    ]
    name = models.CharField(max_length=128,verbose_name="标签名称")
    status = models.IntegerField(default=1,choices=STATUS,verbose_name="标签状态")
    created_time = models.DateTimeField(auto_now=True, editable=False, verbose_name="创建时间")

    owner = models.ForeignKey(User,verbose_name="发布者")

class CONTENT(models.Model):
    STATUS = [
        (0, '已删除'),
        (1, '生效中'),
    ]
    TYPE=[
        (0,'作业'),
        (1,'说明'),
        (2,'提醒')
    ]
    type = models.IntegerField(choices=TYPE,verbose_name="类型")
    title =  models.CharField(max_length=255,verbose_name="标题")
    content = models.CharField(max_length=1024,verbose_name="发布评论")
    status = models.IntegerField(default=1,choices=STATUS,verbose_name="评论状态")
    created_time = models.DateTimeField(auto_now=True, editable=False, verbose_name="创建时间")

    owner = models.ForeignKey(User, verbose_name="发布者")

class COURSE(models.Model):
    TYPE=[
        (0,'课程包'),
        (1,'单节课程'),
    ]
    type = models.IntegerField(choices=TYPE,verbose_name="课程类型")
    # ’单节课程‘可以从属于一个课程包，也可以为0； ’课程包‘ 该参数为null
    father_ID = models.IntegerField(verbose_name="所属课程包")
    name = models.CharField(max_length=128,verbose_name="名称")
    classroom = models.CharField(max_length=256,verbose_name="课程地点")
    start_time = models.DateTimeField(auto_now=True,editable=False,verbose_name="开始时间")
    end_time = models.DateTimeField(auto_now=True,editable=False,verbose_name="结束时间")
    created_time = models.DateTimeField(auto_now=True, editable=False, verbose_name="创建时间")

    #课程对应的评论，标签，发布者
    content = models.ForeignKey(CONTENT,verbose_name="评论")
    label = models.ForeignKey(LABEL,verbose_name="标签")
    owner = models.ForeignKey(User, verbose_name="发布者")




    '''
    根据个人信息返回近一周课表
    
    '''

class WechatLoginView(APIView):

    def WXLogin(self, request):




