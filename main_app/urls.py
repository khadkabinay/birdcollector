from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='birds_index'),
    path('birds/<int:bird_id>/', views.birds_detail, name='detail'),
    path('birds/<int:bird_id>/delete/', views.birds_delete, name='birds_delete'),
    path('birds/<int:bird_id>/edit/', views.birds_edit, name='birds_edit'),
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding'),

]