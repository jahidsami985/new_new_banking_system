from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin_view, name='signin'),  # root URL '/'
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
    path('signout/', views.signout_view, name='signout'),  # <-- enable this!
    path('home/', views.home_view, name='home'), 

]
