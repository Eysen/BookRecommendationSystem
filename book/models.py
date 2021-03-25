from django.db import models


# Create your models here.
from users.models import User

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    book_author = models.CharField(max_length=50)
    book_rating = models.DecimalField(decimal_places=1,max_digits=6,default=0)
    book_author = models.CharField(max_length=50,null=True)
    book_isbm = models.CharField(max_length=200)
    press_information = models.CharField(max_length=200)
    book_profile_photo = models.ImageField(upload_to='book_img', default='book_img/default.jpg',null=True)
    book_profile = models.TextField(null=True, blank=True)
    # 定义在admin后台显示的字段
    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    # 获取书名
    def get_book_name(self):
        return self.book_name

    # 获取评分
    def get_rating(self):
        return self.book_rating


class BookandUser(models.Model):
    book_pk = models.CharField(max_length=200)
    user_pk = models.CharField(max_length=200)
    rate_book_by_user = models.DecimalField(decimal_places=1,max_digits=6,default=0)
    book_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    # book_detail = author = models.OneToOneField('book', on_delete=models.CASCADE)
    # 定义在admin后台显示的字段
    class Meta:
        verbose_name = "book_rating_by_user"
        verbose_name_plural = "books_rating_by_users"

    # 获取书名
    def get_book_name(self):
        return self.book_pk

    # 获取评分
    def get_rating(self):
        return self.user_pk

    def get_rate_book_by_user(self):
        return self.rate_book_by_user