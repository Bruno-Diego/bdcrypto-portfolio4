from django.contrib import admin
from home.models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('user', 'name', 'created_on')
    list_display = ('name', 'user', 'created_on')
    search_fields = ['name', 'user']
