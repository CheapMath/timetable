from django.contrib import admin

# Register your models here.
from ttable import models
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','grades','classes','birth','status','created_time')
    list_filter = ('sex','status','grades','classes','created_time')
    search_fields = ('name',)
    fieldsets = (
        (None,{
         'fields':(
             'name',
             ('sex','birth'),
             ('grades','classes'),
             'status',
         )
        }),
    )

@admin.register(models.USER)
class USERAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','cellphone','email','avatar','status','openid','admin_type','created_time')
    list_filter = ('admin_type',)

@admin.register(models.Student_USER)
class Student_USER_Admin(admin.ModelAdmin):
    list_display = ('student', 'user', 'relation_type')
    list_filter = ('relation_type',)

#admin.site.register(models.UserProfile)