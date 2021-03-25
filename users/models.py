from django.db import models

# Create your models here.
from taggit.managers import TaggableManager

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager
)


class UserManager(BaseUserManager):

    def create_user(self, username, email, password, **kwargs):
          """
        创建普通用户
        """
        # 创建用户前，判断email地址是否合法
          if not email:
            raise ValueError("Users must have a valid email address.")


          user = self.model(username = username,email = self.normalize_email(email),first_name = kwargs.get('first_name'),last_name=kwargs.get('last_name'),)
        # 将用户密码作为hash存储
          user.set_password(password)
          user.is_user = True
          user.save()
          return user

    def create_superuser(self, username, email, password=None, **kwargs):
        """
        创建超级用户
        """

        # 先创建普通用户
        user = self.create_user(
            username, email, password, **kwargs
        )

        user.is_user = True
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField() # 邮箱，唯一属性

    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    # 此部分属性可在个人信息页面修改
    profile_photo = models.ImageField(upload_to='pic_folder', default='pic_folder/default.jpg')
    profile = models.TextField(null=True, blank=True)
    # skills = TaggableManager(blank=True)

    # 用户角色定义，自由管理员/用户
    # is_admin = models.BooleanField('project_owner status', default=False)
    is_user = models.BooleanField('user status', default=True)

    date_created = models.DateTimeField(auto_now_add=True) # 创建用户时间
    date_modified = models.DateTimeField(auto_now=True) # 修改用户时间

    is_admin = models.BooleanField(default=False) # 如果用户具有所有权限，值为True。
    is_superuser = models.BooleanField(default=False) # 如果用户具有所有权限，值为True。
    is_staff = models.BooleanField(default=False) # 如果用户被允许访问管理界面，值为 True。
    is_active = models.BooleanField(default=True) # 如果用户帐户当前处于活动状态，值为True。

    objects = UserManager()    # 下一节讲解manager

    USERNAME_FIELD = 'username' # 描述用户模型上用作唯一标识符的字段名称的字符串。
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name'] # 通过createsuperuser管理命令创建用户时将提示的字段名称列表。

     # 定义在admin后台显示的字段
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    # 获取名字缩写
    def get_short_name(self):
        return self.first_name

    # 获取全名
    def get_full_name(self):
        if self.first_name:
            first_name = ' '.join(
                [i.capitalize() for i in self.first_name.split(' ')]
            )
            last_name = ' '.join(
                [i.capitalize() for i in self.last_name.split(' ')
                 if self.last_name]
            )
            full_name = [first_name, last_name]
            full_name = ' '.join(
                [i.strip() for i in full_name if i.strip()]
            )

            return full_name
        else:
            return "%s" % (self.email)
