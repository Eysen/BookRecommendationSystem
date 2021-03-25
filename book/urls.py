from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from users.views import FreelancerSignUpView, FreelancerSignUpForm, OwnerSignUpView
from .views import (
    BookDetailView, Book_rating_by_UserView, Book_list, BookDetaiWithoutUserView,
    # UpdateProfileView,
    # SignUpView
    # UserJobProfile,
)

app_name = 'book'

urlpatterns = [
    path('book/', include([
        path('book_detail/<str:book_id>/', BookDetailView.as_view(), name='book_detail'),
        path('book_detail_without_user/<str:book_id>/', BookDetaiWithoutUserView.as_view(), name='book_detail_without_user'),
        path('book_rating/<str:book_id>/', Book_rating_by_UserView.as_view(),name='book_rating'),
        path('book_list/',Book_list.as_view(),name='book_list')
        # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
        # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        # path('signup/', SignUpView.as_view(), name='signup'),
        # path('signup/project-owner/',OwnerSignUpView.as_view(),name='project-owner'),
        # path('signup/freelancer/', FreelancerSignUpView.as_view(), name='freelancer_signup'),
    ])),
    # path('freelancers/', include([
        # path('', ListFreelancersView.as_view(), name='list_freelancer'),
    # ])),
    # path('user/', include([
    #     path('<str:pk>/edit', UpdateProfileView.as_view(), name="update_profile"),
    #     path('<str:username>/', UserDetailView.as_view(), name='user_profile'),
    #     # path('<str:username>/jobs/', UserJobProfile.as_view(), name='job_profile'),
    # ])),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
