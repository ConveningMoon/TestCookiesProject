from django.urls import path
from . import views

urlpatterns = [
    path('testcookie/', views.cookie_session, name='cookie_session'),
    path('deletecookie/', views.cookie_delete, name='cookie_delete'),
    path('create/', views.create_session, name='create_session'),
    path('access/', views.access_session, name='access_session'),
    path('delete/', views.delete_session, name='delete_session'),
]
