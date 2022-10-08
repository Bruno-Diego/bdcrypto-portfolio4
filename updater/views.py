from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from updater.models import Crypto
# Create your views here.


class CryptoView(TemplateView):
    """
    This class creates the view for the
    data sent from the API and render the last record
    """
    def get(self, request, **kwargs):
        latest_coins = Crypto.objects.latest('timestamp')
        coins = latest_coins.coins
        timestamp = "{t.year}/{t.month:02d}/{t.day:02d} - {t.hour:02d}:{t.minute:02d}:{t.second:02d}".format(t=latest_coins.timestamp)

        return render(
            request,
            'crypto.html',
            {
                'coins':coins,
                'utc_update_times': timestamp})
