from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView, RedirectView, ListView
from book.models import Book, BookandUser




class BookDetailView(TemplateView):
    model = Book
    template_name = 'book/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        # print(self.request.session.get('_auth_user_id'))
        # [’_auth_user_id’, ‘_auth_user_backend’, ‘_auth_user_hash’]
        book_id = self.kwargs.get('book_id')
        context['book_detail'] = Book.objects.get(id=int(book_id))
        context['user_detail'] = BookandUser.objects.get(user_pk=self.request.session.get('_auth_user_id'), book_pk=book_id)
        return context


class BookDetaiWithoutUserView(TemplateView):
    model = Book
    template_name = 'book/book_detail_withoutUser.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetaiWithoutUserView, self).get_context_data(**kwargs)
        book_id = self.kwargs.get('book_id')
        context['book_detail'] = Book.objects.get(id=book_id)
        return context


class Book_rating_by_UserView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'book:book_detail'

    def get_redirect_url(self, *args, **kwargs):
        print(self.request.session.get('_auth_user_id'))
        bookanduser = get_object_or_404(BookandUser, book_pk=kwargs['book_id'], user_pk=self.request.session.get('_auth_user_id'))
        # bookanduser.rate_book_by_user = kwargs.get('rating')
        bookanduser.rate_book_by_user = self.request.POST.get('rating')
        bookanduser.save()
        return super().get_redirect_url(*args, book_id=kwargs['book_id'])


class Book_list(ListView):
    model = Book
    ordering = ('id',)
    context_object_name = 'books'
    template_name = 'book/book_list.html'
    queryset = Book.objects.all()
