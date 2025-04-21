from django.urls import path
from . import views

urlpatterns = [
    path('regester/', views.regesterpage, name='regester'),
    path('login/', views.loginpage, name='login'),


    path('', views.home, name='home'),
    path('update_data/<int:id>/', views.update_data, name='edit_grocery'),
    path('delete_data/<int:id>/', views.delete_data, name='delete_grocery')
]