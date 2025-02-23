from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
    path('about/', views.aboutPage, name='aboutpage'),
]