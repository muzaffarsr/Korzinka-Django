from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='manage'),
    path('search_admin/', views.search_admin, name='search_admin'),
    path('categorys/', views.categorys, name='categorys'),
    path('search_category/', views.search_category, name='search_category'),
    path('edit/<pid>/', views.edit, name='edit'),
    path('remove/<pid>/', views.remove, name='remove'),
    path('edit-category/<cid>/', views.edit_category, name='edit-category'),
    path('remove-category/<cid>/', views.remove_category, name='remove-category'),
]
