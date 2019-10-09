from django.shortcuts import render
from rest_framework import viewsets
from .models import COURSE
from .serializers import CourseSerializers
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序,负号代表降序
    queryset = COURSE.objects.all().order_by('-id')

    serializer_class = CourseSerializers



class student_course:


    def __init__(self,data):
        pass
    '''
    根据userid获取studentid
    '''


    '''
    根据解析出来的userid 获取 user 信息
    '''
    def get_course(self,user_id):
        return True;
    '''
    根据解析出来的userid 获取 studentid 再获取该student的course信息
    '''
    def add_course_package(self):
        return True;

    '''
    根据studentid 获取
    '''
    def add_course(slef):
        return True;

    def modify_course(get_course):
        return True;

