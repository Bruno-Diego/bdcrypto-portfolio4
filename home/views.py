from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from .models import Portfolio, Asset
from .forms import AssetForm, AssetUpdateForm


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
        messages.success(self.request, 'You are registered and logged in!')
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
        messages.success(self.request, 'You are logged in!')
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


class PortfolioCreate(LoginRequiredMixin, CreateView):
    '''
    View for the creation of a portfolio
    '''
    model = Portfolio
    fields = ['name']
    success_url = reverse_lazy('portfolios')
    template_name = 'home/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form['name'].value())
        messages.success(self.request, 'Portfolio created!')
        return super(PortfolioCreate, self).form_valid(form)


class PortfolioUpdate(LoginRequiredMixin, UpdateView):
    '''
    View for the update of a portfolio
    '''
    model = Portfolio
    fields = ['name']
    success_url = reverse_lazy('portfolios')
    template_name = 'home/create.html'

    def form_valid(self, form):
        form.instance.slug = slugify(form['name'].value())
        messages.success(self.request, 'Portfolio updated!')
        return super(PortfolioUpdate, self).form_valid(form)
    

class PortfolioDetail(LoginRequiredMixin, DetailView, CreateView):
    model = Portfolio
    context_object_name = 'portfolio'
    template_name = 'home/portfolio.html'
    form_class = AssetForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assets'] = Asset.objects.all().filter(portfolio_name=context['portfolio'])
        context['asset_form'] = AssetForm()
        context['asset_update_form'] = AssetUpdateForm()
        return context

    def post(self, request, slug, *args, **kwargs):
        queryset = Portfolio.objects.filter(user=self.request.user)
        portfolio = get_object_or_404(queryset, slug=slug)
        asset_form = AssetForm(data=request.POST)
        if asset_form.is_valid():
            asset_form.instance.portfolio_name = portfolio
            asset_form.save()
            messages.success(self.request, 'Asset added!')
            return self.form_valid(asset_form)
        else:
            asset_form = AssetForm()
   
    def get_success_url(self):
        slug=self.kwargs['slug']
        return reverse_lazy('portfolio', kwargs={'slug': slug})


class PortfolioDelete(LoginRequiredMixin, DeleteView):
    model = Portfolio
    context_object_name = 'portfolio'
    success_url = reverse_lazy('portfolios')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Portfolio DELETED!')
        return super(PortfolioDelete, self).delete(request, *args, **kwargs)

class home_page(TemplateView):
    '''Function to display the home page'''
    template_name = 'home/index.html'

class AssetUpdate(LoginRequiredMixin, UpdateView):
    model = Asset
    form_class = AssetUpdateForm
    template_name = 'home/updateasset.html'

    def get_success_url(self):
        slug=self.kwargs['slug']
        return reverse_lazy('portfolio', kwargs={'slug': slug})

    # def post(self, request, slug, id, *args, **kwargs):
    #     queryset = Asset.objects.filter(user=self.request.user)
    #     portfolio = get_object_or_404(queryset, slug=slug)
    #     asset = get_object_or_404(queryset, id=id)
    #     asset_update_form = AssetUpdateForm(data=request.POST)
    #     if asset_update_form.is_valid():
    #         asset_update_form.save()
    #         messages.success(self.request, 'Asset updated!')
    #         return self.form_valid(asset_update_form)
    #     else:
    #         asset_update_form = AssetUpdateForm()
