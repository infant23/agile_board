from django.urls import path
from .views import *


app_name = 'board'
urlpatterns = [
	path('', TaskList.as_view(), name='index'),
	path('<int:pk>/update/', TaskUpdate.as_view(), name='task_update_url'),
	path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete_url'),
	path('<int:pk>/leave/', TaskLeave.as_view(), name='task_leave_url'),
	path('<int:pk>/process/', TaskProcess.as_view(), name='task_process_url'),
	path('<int:pk>/done/', TaskDone.as_view(), name='task_done_url'),
]
