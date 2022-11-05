from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('random/', views.random, name='random'),
    path('<short_id>/', views.redirect_url, name='redirect'),
]