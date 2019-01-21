from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Task
# from .forms import TaskTextForm


# class TaskCRUMixin(LoginRequiredMixin, View):
# 	model = Task
# 	model_form = TaskTextForm
# 	page = 'board:index'
# 	raise_exception = True
# 	lst = None
# 	task = None
# 	form = None
# 	template = None

# 	def get(self, request):
# 		self.lst = self.model.objects.filter(user_id=request.user)
# 		context={
# 			'tasks_todo': self.lst.filter(state='T'),
# 			'tasks_now': self.lst.filter(state='P'),
# 			'tasks_done': self.lst.filter(state='D'),
# 			'task': self.task,
# 			'form': self.form,
# 			'user': request.user
# 		}
# 		return render(request, self.template, context=context)

# 	def post(self, request):
# 		self.lst = self.model.objects.filter(user_id=request.user)
# 		context={
# 			'tasks_todo': self.lst.filter(state='T'),
# 			'tasks_now': self.lst.filter(state='P'),
# 			'tasks_done': self.lst.filter(state='D'),
# 			'task': self.task,
# 			'form': self.form,
# 			'user': request.user
# 		}
# 		return render(request, self.template, context=context)



class ChangeStateMixin(LoginRequiredMixin, View):
	model = Task
	page = 'board:index'
	raise_exception = True
	state = None

	def post(self, request, pk):
		obj = get_object_or_404(self.model, pk=pk, user_id=request.user)
		obj.state = self.state
		obj.save()
		return redirect(reverse(self.page))
