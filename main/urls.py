from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('accept/', views.accept, name='accept'),
    path('thanks/', views.thanks, name='thanks'),
    path('product/<pid>', views.product, name='product'),
    path('category/<cid>', views.category, name='category'),
]
