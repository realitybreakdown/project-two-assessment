from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Widget
from django.views.generic import TemplateView
from .forms import WidgetForm



# Create your views here.

def index(request):
    return render(request, 'index.html')

class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'
    template_name = 'index.html'

    def get_success_url(self, **kwargs):
        return('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['widgets'] = Widget.objects.all()
        return context