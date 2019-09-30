from django.urls import path #导入path方法
from course import views #从本app目录导入views

urlpatterns = [
    path('get_course', views.student_course.get_course),  #获取自定义时间课程
    path('add_course_package',views.student_course.add_course_package), #添加课程包
    path('add_course',views.student_course.add_course), #添加课程
    path('modify_course',views.student_course.modify_course), #修改课程
]

