from django.urls import path #导入path方法
from . import views #从本app目录导入views

urlpatterns = [
    path('get_course', views.get_course),
    path('add_course_package',views.add_course_package),
    path('add_course',views.add_course),
    path('modify_course',views.modify_course),
]

