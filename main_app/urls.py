from django.urls import path 
from . import views 

urlpatterns = [
    path('/hhh', views.index, name='index'),
    path('', views.WidgetCreate.as_view(), name='widget_create'),

]