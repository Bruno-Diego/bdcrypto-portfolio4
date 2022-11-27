from django import forms
from .models import Asset
from .cryptoapi import update_coins

coins_list = update_coins()

SELECT_CRYPTO = []

for coin in coins_list:
    SELECT_CRYPTO.append((coin['symbol'], coin['name'] + ' is currently: $' + coin['price']))


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('symbol', 'quantity')
        labels = {'symbol': ('Choose an asset to buy:')}
        widgets = {
            'symbol': forms.Select(attrs={'class':'input-field'}, choices=SELECT_CRYPTO),
        }


class AssetUpdateForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('quantity',)
