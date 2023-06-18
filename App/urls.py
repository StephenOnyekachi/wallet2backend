from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('usersignup1/', views.usersignup1, name='usersignup1'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('edithprofile/<int:pk>/', views.edithprofile, name='edithprofile'),

    path('adminpage', views.adminpage, name='adminpage'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('deposit', views.deposit, name='deposit'),
    path('messagedelete/<int:pk>/', views.messagedelete, name='messagedelete'),
    path('message', views.message, name='message'),
    path('messagesView', views.messages, name='messages'),
    path('paymentdelete/<int:pk>/', views.paymentdelete, name='paymentdelete'),
    path('paymentedit', views.paymentedit, name='paymentedit'),

    path('profile/<int:pk>/', views.profile, name='profile'),
    path('user/<int:pk>/', views.user, name='user'),
    path('userblock/<int:pk>/', views.userblock, name='userblock'),

    path('userdelete/<int:pk>/', views.userdelete, name='userdelete'),
    path('useredit/<int:pk>/', views.useredit, name='useredit'),
    path('users', views.users, name='users'),

    path('walletdelete/<int:pk>/', views.walletdelete, name='walletdelete'),
    path('walletedit', views.walletedit, name='walletedit'),
    path('withdraw', views.withdraw, name='withdraw'),

]
