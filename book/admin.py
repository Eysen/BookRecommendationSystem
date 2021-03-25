from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin,UserAdmin

from .models import Book ,BookandUser
from .forms import BookCreationForm, BookChangeForm\
    ,Book_UserCreationForm,Book_UserChangeForm

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # 定义修改和添加表单
    form = BookChangeForm
    add_form = BookCreationForm

    # 用于显示用户模型的字段
    # 这些会覆盖原本UserAdmin的定义
    list_display = ('book_name','book_author','pub_date','book_isbm', 'book_rating','press_information','book_profile_photo','book_profile')    #定义在管理员后台显示的字段
    list_filter = ('book_name',)   #通过list_filter函数来过滤
    #编辑用户 修改内容时显示的字段   可以分组
    fieldsets = (
        (None, {'fields': ('book_name','book_author', 'pub_date','book_isbm',)}),
        ('People Rating info', {'fields': ('book_rating',)}),
        ('Press Information', {'fields': ('press_information',)}),
        ('Book_detail',{'fields':('book_profile_photo','book_profile')})
    )

    # add_fieldsets不是标准的ModelAdmin属性
    # UserAdmin会在创建时使用此属性覆盖掉get_fieldsets
    #创建用户时使用
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('book_name','book_author', 'pub_date', 'book_isbm','book_rating', 'press_information','book_profile_photo','book_profile')}
        ),
    )
    search_fields = ('book_name',)  #以邮箱查找
    ordering = ('book_name',)   #以邮箱排序
    filter_horizontal = ()    #设置过滤器样式




class Book_UserAdmin(admin.ModelAdmin):
    # 定义修改和添加表单
    form = Book_UserChangeForm
    add_form = Book_UserCreationForm

    # 用于显示用户模型的字段
    # 这些会覆盖原本UserAdmin的定义
    list_display = ('book_name','username','rate_book_by_user','book_pk','user_pk',)  # 定义在管理员后台显示的字段
    # list_filter = ('is_admin',)  # 通过list_filter函数来过滤
    # 编辑用户 修改内容时显示的字段   可以分组
    fieldsets = (
        (None, {'fields': ('book_pk','user_pk')}),
        ('Name',{'fields':('book_name','username')}),
        ('Rating info', {'fields': ('rate_book_by_user',)}),
   )

    # add_fieldsets不是标准的ModelAdmin属性
    # UserAdmin会在创建时使用此属性覆盖掉get_fieldsets
    # 创建用户时使用
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('book_pk','user_pk','book_name','username', 'rate_book_by_user',)}
         ),
    )
    search_fields = ('book_pk',)  # 以邮箱查找
    ordering = ('book_pk',)  # 以邮箱排序
    filter_horizontal = ()  # 设置过滤器样式



# # 组成自己写的User和UserAdmin
# admin.site.register(Book,BookAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(BookandUser,Book_UserAdmin)
# # 因为我们自己设计了用户权限，没有使用Django内建的权限机制，所以在这里从admin中注销Group
# admin.site.unregister(Group)