from django.urls import path

from . import views

urlpatterns = [
    path('', views.title, name='title'),
    path('sign', views.sign, name='sign'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('lobby', views.lobby, name='lobby'),
    path('chat', views.room, name='room'),
]