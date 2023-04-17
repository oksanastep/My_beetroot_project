from django.urls import path
from django.contrib.auth.views import LoginView
from .views import HomePageView, SearchResultsView, SearchContainer,  SearchAlphabet, register_request, login_request, \
    logout_request, AboutUs


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("search-container/", SearchContainer.as_view(), name="search_container"),
    path("search-results/", SearchResultsView.as_view(), name="search_results"),
    path("search-alphabet/", SearchAlphabet.as_view(), name="search_alphabet"),
    path("about_us", AboutUs.as_view(), name="about_us"),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),

]
