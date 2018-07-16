
from django.contrib import admin
from django.urls import path
from SolarDB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('homepage/', views.homepage, name='homepage'),
    path('displaypost/', views.displaypost, name='displaypost'),
    path('addpost/', views.addpost, name='addpost'),
    path('logout/', views.logout, name = "logout"),
]
