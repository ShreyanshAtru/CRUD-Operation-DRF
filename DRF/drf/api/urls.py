from django.contrib import admin
from django.urls import path, include
from . import views
from .views import UserRegistrationView
urlpatterns = [
    path('',views.apiOverview, name='api-overview'),
    path('task-list/',views.tasklist, name='task-list/'),
    path('task-detail/<str:pk>/',views.taskdetail, name='task-detail/'),
    path('task-create/',views.taskcreate, name='task-create/'),
    path('task-update/<str:pk>/',views.taskupdate, name='task-update/'),
    path('task-delete/<str:pk>/',views.taskdelete, name='task-delete/'),
    path('customer/register', UserRegistrationView.as_view()),
]
