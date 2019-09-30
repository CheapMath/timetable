from django.contrib import admin

# Register your models here.
'''
# listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('name', 'sex', 'age', 'TEL', 'member_type')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-name',)
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top =True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段（name默认不可编辑，因为它是一个链接，点击会进入修改页面）
    list_editable = ['TEL', 'member_type',]
    # fk_fields 设置显示外键字段
    fk_fields = ('member_type',)
    # 过滤器功能及能过滤的字段
    list_filter = ('name', 'member_type')  
    # 搜索功能及能实现搜索的字段
    search_fields = ('name', 'TEL', )  

'''
from ttable import models
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','grades','classes','birth','status','created_time')
    list_editable = ['name','sex','grades','classes','birth','status', ]
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

@admin.register(models.User)
class USERAdmin(admin.ModelAdmin):
    list_display = ('id','username','gender','email','avatar_url','openid','cellphone','created_time','is_active')
    list_editable = ['username','email','cellphone','is_active']
    list_filter = ('openid','created_time','is_active')
    search_fields = ('cellphone','openid')

