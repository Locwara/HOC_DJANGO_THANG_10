
from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.get_index),
    path('index/', views.get_index1, name='trangchu')
]