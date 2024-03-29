# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.tasklist, name='task'),
# ]

from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('', TaskList.as_view(), name='task'),
    path('detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    
] 
