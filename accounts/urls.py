
from django.urls import path

from . import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('create_article/', views.create_article, name='create_article'),
    path('home/',views.home,name='home'),
    path('home/<int:id>/',views.article_detail,name='article_detail'),
    path('contact/',views.contact,name='contact')
]