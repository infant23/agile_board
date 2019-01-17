from django import forms
from .models import Task
from django.core.exceptions import ValidationError


class TaskTextForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ['content']

		widgets = {
			'content': forms.Textarea(attrs={'class': 'form-control'})
		}
