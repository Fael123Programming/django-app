from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post', views.post_list, name='post_list'),
    path('post/<str:pk>', views.post, name='post')  # <type:name>, dynamic url routing.
]
