from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('account/signup/', views.signupView, name='signup'),
    path('account/login/', views.loginView, name='login'),
    path('account/logout/', views.logoutView, name='logout'),
    path('category/<slug:category_slug>', views.home, name='bikes_by_category'),
    path('category/<slug:category_slug>/<slug:bike_slug>', views.detail, name='bike_detail'),

]