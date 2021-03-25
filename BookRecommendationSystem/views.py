from django.shortcuts import render
from book.models import  Book

def home(request):
    book_all = Book.objects.all()
    return render(request,'home.html',{'book_all':book_all})


def basete(request):
    return render(request,'base.html')



