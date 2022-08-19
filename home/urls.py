from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('portfolios/', views.PortfoliosList.as_view(), name='portfolios'),
    path('portfolios/<slug:slug>/', views.PortfolioDetail.as_view(),
         name='portfolio'),
    path('create/', views.PortfolioCreate.as_view(), name='create'),
    path('update/<slug:slug>/', views.PortfolioUpdate.as_view(), name='update'),
    path('delete/<slug:slug>/', views.PortfolioDelete.as_view(), name='delete'),
    path('', views.home_page, name='home-page'),
]
