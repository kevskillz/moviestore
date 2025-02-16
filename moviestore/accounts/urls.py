from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),
    path('forgot_password/', views.forgot_password, name='accounts.forgot_password'),
    path('set_new_password/<str:username>/', views.set_new_password, name='accounts.set_new_password'),
]