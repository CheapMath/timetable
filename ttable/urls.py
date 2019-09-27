from django.urls import path #导入path方法
from . import views #从ttable目录

urlpatterns = [
    path('user_info', views.get_wx_user_info),
    path('student_info',views.get_student_info),
]

