from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('join_view/', views.join_view),
    path('join_view/join/', views.join, name = 'join')

]