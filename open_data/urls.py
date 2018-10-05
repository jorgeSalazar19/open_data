from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from mysite import views as core_views

urlpatterns = [
    path(r'', core_views.home, name='home'),
    path(r'consulta/', core_views.consulta, name='consulta'),
    path('admin/', admin.site.urls),
    path(r'login/', auth_views.login, name='login'),
    path(r'logout/', core_views.logOut, name='logout'),
    path(r'oauth/', include('social_django.urls', namespace='social')),
]
