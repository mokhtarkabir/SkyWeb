from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.blogPage, name='blogpage'),
]