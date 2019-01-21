from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from time import time


class Task(models.Model):
	TASK_STATE = (
		('T', 'TO DO'),
		('P', 'In progress'),
		('D', 'Done'),
		)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(blank=True, max_length=140)
	state = models.CharField(max_length=20, blank=True, choices=TASK_STATE) 
	pub_date = models.DateTimeField(auto_now_add=True)

	def get_update_url(self):
		return reverse('board:task_update_url', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('board:task_delete_url', kwargs={'pk': self.pk})

	def get_leave_url(self):
		return reverse('board:task_leave_url', kwargs={'pk': self.pk})

	def get_process_url(self):
		return reverse('board:task_process_url', kwargs={'pk': self.pk})

	def get_done_url(self):
		return reverse('board:task_done_url', kwargs={'pk': self.pk})

	def __str__(self):
		return self.content

	class Meta:
		ordering = ['-pub_date']
