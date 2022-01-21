from django.urls import path

from . import views 

app_name = 'blog'

urlpatterns = [

    path('', views.index, name = 'index'),

    path('posts/', views.posts, name = 'posts'),

    path('search/', views.search, name = 'search'),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name = 'post_detail'),

    path('author/', views.author, name = 'author'),

]