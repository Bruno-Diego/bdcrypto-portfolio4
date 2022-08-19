from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Portfolio, Asset


class RegisterPage(FormView):
    '''
    Class for the view of the register page
    '''
    template_name = 'home/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('portfolios')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **hwargs):
        if self.request.user.is_authenticated:
            return redirect('portfolios')
        return super(RegisterPage, self).get(*args, **hwargs)


class CustomLoginView(LoginView):
    '''
    Class of the view for the login page
    '''
    template_name = 'home/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('portfolios')


class PortfoliosList(LoginRequiredMixin, ListView):
    """
    Class of a view created to show the 
    list of portfolios created by the user
    """
    model = Portfolio
    context_object_name = 'portfolios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolios'] = context['portfolios'].filter(user=self.request.user)
        return context


class PortfolioCreate(CreateView):
    '''
    View for the creation of a portfolio
    '''
    model = Portfolio
    fields = '__all__'
    success_url = reverse_lazy('portfolios')
    template_name = 'home/create.html'


class PortfolioDetail(LoginRequiredMixin, DetailView):
    model = Portfolio
    context_object_name = 'portfolio'
    template_name = 'home/portfolio.html'


def home_page(request):
    '''Function to display the home page'''
    return render(request, 'home/index.html')
