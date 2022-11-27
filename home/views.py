from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse
from django.urls import reverse_lazy, resolve
from django.template.defaultfilters import slugify

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from decimal import Decimal

from .models import Portfolio, Asset
from .forms import AssetForm, AssetUpdateForm
from .cryptoapi import update_coins

coins = update_coins()


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
    

class PortfolioDetail(LoginRequiredMixin, DetailView):
    model = Portfolio
    context_object_name = 'portfolio'
    template_name = 'home/portfolio.html'
    form_class = AssetUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for asset in Asset.objects.all():
            symbol_field = Asset._meta.get_field('symbol')
            symbol_value = symbol_field.value_from_object(asset)
            current_price_field = Asset._meta.get_field('current_price')
            current_price_value = current_price_field.value_from_object(asset)
            buy_price_field = Asset._meta.get_field('buy_price')
            buy_price_value = buy_price_field.value_from_object(asset)
            pnl_updated = float(current_price_value) - float(buy_price_value)
            if float(current_price_value) > float(buy_price_value):
                earnings = pnl_updated
            Asset.objects.filter(id=asset.id).update(current_price=get_coin_details(symbol_value, coins)[1], pnl=pnl_updated, usd_earned=earnings)
        context['assets'] = Asset.objects.all().filter(portfolio_name=context['portfolio'])
        context['cryptolist'] = update_coins()
        context['asset_update_form'] = AssetUpdateForm()
        return context
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Portfolio.objects.filter(user=self.request.user)
        portfolio = get_object_or_404(queryset, slug=slug)
        asset_update_form = AssetUpdateForm(data=request.POST)
        if asset_update_form.is_valid():
            asset_update_form.instance.portfolio_name = portfolio
            asset_update_form.save()
            messages.success(self.request, 'Asset added!')
            return self.form_valid(asset_update_form)
        else:
            asset_update_form = AssetForm()
    
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Portfolio.objects.filter(user=self.request.user)
        context['portfolio'] = get_object_or_404(queryset, name=context['asset'].portfolio_name)
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['quantity'] = ''
        return initial
        
    def form_valid(self, AssetUpdateForm):
        if resolve(self.request.path_info).url_name == 'buyasset':
            AssetUpdateForm.instance.quantity += self.get_object().quantity
        elif resolve(self.request.path_info).url_name == 'sellasset':
            if AssetUpdateForm.instance.quantity > self.get_object().quantity:
                messages.warning(self.request, 'You can only sell the amount you hold! Please insert another value below.')
                return self.form_invalid(AssetUpdateForm)
            elif AssetUpdateForm.instance.quantity == self.get_object().quantity:
                slug=self.kwargs['slug']
                deleteasset = AssetUpdateForm.save()
                return redirect('assetdelete', slug=slug, pk=deleteasset.id)
            else: 
                AssetUpdateForm.instance.quantity = self.get_object().quantity - AssetUpdateForm.instance.quantity
        messages.success(self.request, 'Portfolio updated!')
        return super(AssetUpdate, self).form_valid(AssetUpdateForm)


def get_coin_details(symbol, coins):
    """
    Will get the price of a coin
    """
    for x in coins:
        if x['symbol'] == symbol:
            rank = x['rank']
            price = float((x['price']))
            icon = x['iconUrl']
    return (rank, price, icon)
