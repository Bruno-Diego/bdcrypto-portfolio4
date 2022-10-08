from django.contrib import admin

# Register your models here.
from updater.models import Crypto

@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = ('coins', 'timestamp')
    search_fields = ['coins']
    list_filter = ('coins', 'timestamp')
    