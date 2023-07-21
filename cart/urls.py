from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', include('allauth.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('upload-profile-pic/', views.upload_profile_pic, name='uploaddp'),
]
