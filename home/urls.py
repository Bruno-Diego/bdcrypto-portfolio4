from django.urls import path, include
from .views import PortfoliosList, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', PortfoliosList.as_view(), name='portfolios'),
]
