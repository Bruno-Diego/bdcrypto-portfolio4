from django.db import models

# Create your models here.
from datetime import datetime 

class Crypto(models.Model):
    """
    This is a model to store the JSON data
    sent from the API to update and validade the coins
    """
    coins = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamps = datetime.utcnow()
        return super(Crypto, self).save(*args, **kwargs)
