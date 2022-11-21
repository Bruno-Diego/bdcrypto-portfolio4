from .models import Asset
from django import forms


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('__all__')
        exclude = ('portfolio_name',)

class AssetUpdateForm(forms.ModelForm):
    quantity = forms.DecimalField(initial=0)
    class Meta:
        model = Asset
        fields = ('quantity',)
