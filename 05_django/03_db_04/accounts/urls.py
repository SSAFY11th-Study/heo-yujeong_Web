from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('<int:user_pk>/update/', views.superuser_update, name='superuser_update'),
    path('<int:user_pk>/delete/', views.delete, name='delete'),
]
