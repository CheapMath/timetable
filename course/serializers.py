#使用rest_framework实现序列化

from rest_framework import serializers
from .models import COURSE


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = COURSE  # 指定的模型类
        fields = ('id', 'type', 'name', 'classroom','student_grade', 'descripe', 'start_time', 'end_time',)  # 需要序列化的属性

