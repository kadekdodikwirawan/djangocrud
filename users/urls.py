from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addUser, name='add_user'),
    path('<int:user_id>/', views.getUser, name='get_user'),
    path('delete/<int:user_id>/', views.deleteUser, name='delete_user'),
    path('update/<int:user_id>/', views.updateUser, name='delete_user'),
]