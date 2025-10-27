
from django.urls import path

from . import views
urlpatterns = [
    path('',views.signup,name='signup'),
    # path('create_article/', views.create_article, name='create_article'),
    path('home/',views.home,name='home'),
    path('home/<int:id>/',views.article_detail,name='article_detail'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login_user,name='login'),
    path('admin-dashboard/',views.admin_dashboard,name='admin-dashboard'),
    path('create-article/',views.create_article,name='admin-create-article'),
    path('list-article/',views.list_article,name='admin-list-article'),
    path('edit-article/<int:id>/',views.edit_article,name='edit-article')
]