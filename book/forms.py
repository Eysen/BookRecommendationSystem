from django import forms
from django.db import models
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction
from .models import Book, BookandUser
from users.models import User


class BookCreationForm(forms.ModelForm):
    """
    创建书籍的表单。
    """
    book_name = forms.CharField(max_length=30, required=True, help_text='书名')
    pub_date = forms.CharField(max_length=30, required=True, help_text='发布时间')
    book_isbm = forms.CharField(max_length=30, required=True, help_text='ISBM码')
    book_rating = forms.EmailField(max_length=254, required=True, help_text='评分')
    press_information = forms.CharField(label= '出版商信息',help_text='出版商信息')
    book_profile_photo = models.ImageField(upload_to='book_img', default='book_img/default.jpg', null=True)
    book_profile = models.TextField(null=True, blank=True)

    class Meta:
         # 注册表单字段
        model = Book
        fields = ('book_name', 'pub_date', 'book_isbm', 'book_rating', 'press_information','book_profile_photo','book_profile')

    # def clean_password(self):
    #     # 检查两次密码是否相同
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match.")
    #     return password2

    def save(self, commit=True):
        # 以哈希格式存储密码
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class BookChangeForm(forms.ModelForm):
    """
    A form for updating users.
    Includes all the fields on the user, but replaces the
    password field with admin's password hash display field.
    """
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = Book
        fields = ('book_name', 'pub_date', 'book_isbm', 'book_rating', 'press_information','book_profile_photo','book_profile')

    # def clean_password(self):
    #     # Regardless of what the user provides, return the initial value.
    #     # This is done here, rather than on the field, because the
    #     # field does not have access to the initial value.
    #     return self.initial["password"]


class Book_UserCreationForm(forms.ModelForm):
    book_pk = models.CharField(max_length=255)
    user_pk = models.CharField(max_length=255)
    rate_book_by_user = models.IntegerField()


    class Meta:
        model = BookandUser
        fields = ('book_pk','user_pk','rate_book_by_user')

    def save(self, commit=True):
            # 以哈希格式存储密码
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class Book_UserChangeForm(forms.ModelForm):
    class Meta:
        model = BookandUser
        fields = ('book_pk', 'user_pk', 'rate_book_by_user')