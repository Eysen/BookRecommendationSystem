from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    # 定义修改和添加表单
    form = UserChangeForm
    add_form = UserCreationForm

    # 用于显示用户模型的字段
    # 这些会覆盖原本UserAdmin的定义
    list_display = ('username','email','date_created', 'is_active','is_admin','is_superuser' ,)    #定义在管理员后台显示的字段
    list_filter = ('is_admin',)   #通过list_filter函数来过滤
    #编辑用户 修改内容时显示的字段   可以分组
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)})
    )

    # add_fieldsets不是标准的ModelAdmin属性
    # UserAdmin会在创建时使用此属性覆盖掉get_fieldsets
    #创建用户时使用
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)  #以邮箱查找
    ordering = ('email',)   #以邮箱排序
    filter_horizontal = ()    #设置过滤器样式


# 组成自己写的User和UserAdmin
admin.site.register(User, UserAdmin)
# 因为我们自己设计了用户权限，没有使用Django内建的权限机制，所以在这里从admin中注销Group
admin.site.unregister(Group)


