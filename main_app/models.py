from django.db import models
from django import forms
from django.urls import reverse

# Create your models here.

class Widget(models.Model):
    description = models.CharField(max_length=50)
    quantity = models.IntegerField(max_length=50)

    def __str__(self):
        return reverse('index')

    def get_absolute_url(self):
       return reverse('index')

class WidgetForm(forms.ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']

    