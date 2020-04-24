from django.contrib import admin
from django.urls import path,include
from contact import views as contact_views

from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('register/',user_views.register,name='register'),
    path('login',user_views.auth_login,name='login'),
    path('logout/',user_views.auth_logout,name='logout'),
]

