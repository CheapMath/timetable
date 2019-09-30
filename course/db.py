from django.http import HttpResponse

from course.models import COURSE
import time

# 数据库操作
def add_course_pakage(request):
    test1 = COURSE(
        name="测试",
        descripe = "无",
        created_time = time.localtime()
    )
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")