from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Index'),
    #path('', views.login_shower, name = 'Index'),
    path('contact/', views.contact, name = 'Contact'),
    path('about/', views.about, name = 'About'),
    path('search/', views.search, name = 'Search'),
    path('signup/', views.signup, name = 'Signup'),
    path('login/', views.handle_login, name = 'Login'),
    path('logout/', views.handle_logout, name = 'Logout'),
    path('con_signup/', views.con_signup, name = 'Con_signup'),
    path('con_login/', views.con_login, name = 'Con_login'),
    path('con_logout/', views.con_logout, name = 'Con_logout'),
]
