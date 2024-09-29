from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/', views.post_list, name='post-list'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/',views.profile,name='profile'),
    path('register/', views.register, name='register'),
    path('blog/new/', views.post_create, name='post-create'),  
    path('blog/<int:pk>/edit/', views.post_update, name='post-update'),  
    path('blog/<int:pk>/delete/', views.post_delete, name='post-delete'),

]