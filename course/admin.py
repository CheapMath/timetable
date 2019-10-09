from django.contrib import admin

# Register your models here.
from course import models
@admin.register(models.COURSE)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'classroom','student_grade', 'descripe', 'start_time', 'end_time','created_time')
    list_editable = ['type', 'name', 'classroom','student_grade', 'descripe',  ]
    list_filter = ('student_grade', 'start_time', 'end_time',)
    search_fields = ('name',)

@admin.register(models.COURSE_PAKAGE)
class Course_PakegeAdmin(admin.ModelAdmin):
    list_display = (
    'id',  'name', 'descripe', 'status', 'descripe', 'owner', 'created_time')
    list_editable = ['name', 'descripe', ]
    list_filter = ('created_time',)
    search_fields = ('name',)


