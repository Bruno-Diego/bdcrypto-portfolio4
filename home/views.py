from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Portfolio, Asset
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin



class CustomLoginView(LoginView):
    '''
    Class of the view for the login page
    '''
    template_name = 'home/login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('portfolios')



class PortfoliosList(LoginRequiredMixin, generic.ListView):
    """
    Class of a view created to show the 
    list of portfolios created by the user
    """
    model = Portfolio


def home_page(request):
    '''Function to display the home page'''
    return render(request, 'home/index.html')
