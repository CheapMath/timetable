from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.




'''
获取信息
'''
class get_info():

    def get_student_info(request):
        return HttpResponse("NAME")


    def get_wx_user_info(request):
        return HttpResponse("name")