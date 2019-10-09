from django.urls import path #导入path方法
from course import views #从本app目录导入views
from django.conf.urls import include,url
from rest_framework import routers

# 定义路由地址
route = routers.DefaultRouter()

# 注册新的路由地址
route.register(r'course', views.CourseViewSet)

urlpatterns = [
    path('course/', include(route.urls)),  #获取自定义时间课程
]

'''
    path('get_course', views.student_course.get_course),  #获取自定义时间课程
    path('add_course_package',views.student_course.add_course_package), #添加课程包
    path('add_course',views.student_course.add_course), #添加课程
    path('modify_course',views.student_course.modify_course), #修改课程
'''

