from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import PortfoliosList, CustomLoginView, RegisterPage, home_page

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('portfolios/', PortfoliosList.as_view(), name='portfolios'),
    path('', home_page, name='home-page'),
]
