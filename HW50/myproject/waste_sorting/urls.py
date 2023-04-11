from django.urls import path
from django.contrib.auth.views import LoginView
from .views import HomePageView, SearchResultsView, AboutYouView, CommentsView, RegisterView
from .forms import AuthenticationFormCustom

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("search-results/", SearchResultsView.as_view(), name="search_results"),
    path("comments/<str:id>/", CommentsView.as_view()),
    path('about_you/', AboutYouView.as_view()),
    path(
        'accounts/login',
        LoginView.as_view(
            authentication_form=AuthenticationFormCustom
        ),
        name='login'
    ),
    path('accounts/register/', RegisterView.as_view(), name='register'),

]
