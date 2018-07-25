from django.urls import path,include
from products.views import*

urlpatterns = [
    path('create',create,name='create'),
    path('<int:product_id>',detail,name='detail'),
    path('<int:product_id>/upvote',upvote,name='upvote'),


]
