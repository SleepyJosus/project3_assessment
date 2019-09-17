from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.ItemCreateView.as_view(), name='add'),
    path('<int:item_id>/delete/', views.item_delete, name='delete'),
]
