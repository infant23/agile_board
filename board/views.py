from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.http import Http404, HttpResponse, HttpResponseRedirect


from .models import Task
from .forms import TaskForm


class TaskList(LoginRequiredMixin, View):
	model = Task
	template = 'board/task_list.html'

	def get(self, request):
		obj = self.model.objects.filter(user_id=request.user)
		context = {
			'tasks_todo': obj.filter(state='T'),
			'tasks_now': obj.filter(state='P'),
			'tasks_done': obj.filter(state='D'),
			'user':request.user
		}
		return render(request, self.template, context=context)


class TaskDetail(LoginRequiredMixin, View):
	model = Task
	template = 'board/task_detail.html'

	def get(self, request, pk):
		context={
			'task': get_object_or_404(self.model, pk=pk),
			'user': request.user
		}
		return render(request, self.template, context=context)


class TaskCreate(LoginRequiredMixin, View):
	model_form = TaskForm
	template = 'board/task_create.html'
	page = 'board:index'
	raise_exception = True

	def get(self, request):
		context={
			'form': self.model_form(),
			'user': request.user
		}
		return render(request, self.template, context=context)

	def post(self, request):
		bound_form = self.model_form(request.POST)
		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(reverse(self.page))
		context={
			'form': bound_form,
			'user': request.user
		}
		return render(request, self.template, context=context)


class TaskUpdate(LoginRequiredMixin, View):
	model = Task
	model_form = TaskForm
	template = 'board/task_update.html'
	page = 'board:index'
	raise_exception = True

	def get(self, request, pk):
		obj = self.model.objects.get(pk=pk)
		bound_form = self.model_form(instance=obj)
		context={
			'task': obj,
			'form': bound_form,
			'user': request.user
		}
		return render(request, self.template, context=context)

	def post(self, request, pk):
		obj = self.model.objects.get(pk=pk)
		bound_form = self.model_form(request.POST, instance=obj)
		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(reverse(self.page))
		context={
			'task': obj,
			'form': bound_form,
			'user': request.user
		}
		return render(request, self.template, context=context)


class TaskDelete(LoginRequiredMixin, View):
	model = Task
	template = 'board/task_delete.html'
	page = 'board:index'
	raise_exception = True

	def get(self, request, pk):
		obj = self.model.objects.get(pk=pk)
		context={
			'task': obj,
			'user': request.user
		}
		return render(request, self.template, context=context)

	def post(self, request, pk):
		obj = self.model.objects.get(pk=pk)
		obj.delete()
		return redirect(reverse(self.page))
