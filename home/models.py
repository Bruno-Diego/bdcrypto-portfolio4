from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Portfolio(models.Model):
    """
    This class defines the Portfolio Model
    that can be created by the user
    """
    name = models.CharField(max_length=9, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
