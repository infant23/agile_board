from django.urls import path
from .views import *


app_name = 'board'
urlpatterns = [
	path('', TaskList.as_view(), name='index'),
	path('create/', TaskCreate.as_view(), name='task_create_url'),
	path('<int:pk>/', TaskDetail.as_view(), name='task_detail_url'),
	path('<int:pk>/update/', TaskUpdate.as_view(), name='task_update_url'),
	path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete_url'),
]
