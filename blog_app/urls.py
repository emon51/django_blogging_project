
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('view_post/<str:id>', views.view_post, name = 'view_post')

]
