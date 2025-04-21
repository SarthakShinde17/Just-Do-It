from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('', views.home, name='home'),
    path('update_data/<int:id>/', views.update_data, name='edit_grocery'),
    path('delete_data/<int:id>/', views.delete_data, name='delete_grocery')
]