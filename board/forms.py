from django import forms
from .models import Task
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['user_id', 'content', 'state']

		widgets = {
			'content': forms.Textarea(attrs={'class': 'form-control'})
		}
