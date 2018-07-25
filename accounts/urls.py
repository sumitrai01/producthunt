from django.urls import path,include
from accounts.views import*

urlpatterns = [
    path('signup',signup,name='signup'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),

]
