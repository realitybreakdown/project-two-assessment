from django.forms import ModelForm, CharField
from .models import Widget

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']