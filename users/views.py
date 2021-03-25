from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.db import models

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login
from django.views.generic import (
    TemplateView, UpdateView,
    CreateView, ListView,
)

from book.models import BookandUser, Book
from .models import User
from .forms import FreelancerSignUpForm, OwnerSignUpForm


class SignUpView(TemplateView):
    template_name = 'users/signup.html'



class UserDetailView(TemplateView):
    model = User
    template_name = 'users/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView,self).get_context_data(**kwargs)
        username = self.kwargs.get('username')
        context['profile'] = User.objects.get(username=username)
        all_rating_book = BookandUser.objects.filter(user_pk = User.objects.get(username=username).id)
        context['all_rating_book'] = all_rating_book
        print([ i.id for i in all_rating_book])
        book_all_img = Book.objects.filter(id__in=[ i.id for i in all_rating_book ])
        context['book_all_img'] = book_all_img
        print([i.id for i in book_all_img])
        print([j.book_profile_photo.url for j in book_all_img] )
        # test =[ i.id for i in all_rating_book ]
        # print(test)
        # print(type(all_rating_book))
        return context


class UpdateProfileView(UpdateView):
    """
    Update the profile.
    """
    model = User
    fields = ['profile_photo', 'first_name', 'last_name', 'profile'] # Keep listing whatever fields
    template_name = 'users/user_profile_update.html'

    def form_valid(self, form):
        """
        Checks valid form and add/save many to many tags field in user object.
        """
        user = form.save(commit=False)

        user.save()
        form.save_m2m()
        messages.success(self.request, 'Your profile is updated successfully.')
        return redirect('users:user_profile', self.object.username)



    def get_success_url(self):
        """
        Prepares success url for successful form submission.
        """
        return reverse('users:user_profile', kwargs={'username': self.object.username})


class FreelancerSignUpView(CreateView):
    """
    Register a freelancer.
    """
    model = User
    form_class = FreelancerSignUpForm
    template_name = 'users/signup_form.html'

    def get_context_data(self, **kwargs):
        """
        Updates context value 'user_type' in curernt context.
        """
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)



    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = 'users/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        owner = form.save()
        login(self.request, owner)
        return redirect('home')

