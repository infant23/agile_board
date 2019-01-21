from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

# from django.http import Http404, HttpResponse, HttpResponseRedirect


from .models import Task
from .forms import TaskTextForm
from .utils import ChangeStateMixin


class TaskList(LoginRequiredMixin, View):
	model = Task
	model_form = TaskTextForm
	template = 'board/index.html'
	page = 'board:index'
	login_url = 'board:login'
	# redirect_field_name = 'board:login'
	# raise_exception = True

	def get(self, request):
		lst = self.model.objects.filter(user_id=request.user)
		context = {
			'tasks_todo': lst.filter(state='T'),
			'tasks_now': lst.filter(state='P'),
			'tasks_done': lst.filter(state='D'),
			'form': self.model_form(),
			'user':request.user
		}
		return render(request, self.template, context=context)

	def post(self, request):
		lst = self.model.objects.filter(user_id=request.user)
		bound_form = self.model_form(request.POST)
		if bound_form.is_valid():
			new_obj = bound_form.save(commit=False)
			new_obj.user_id = request.user
			new_obj.state = "T"
			new_obj.save()
			return redirect(reverse(self.page))
		context={
			'tasks_todo': lst.filter(state='T'),
			'tasks_now': lst.filter(state='P'),
			'tasks_done': lst.filter(state='D'),
			'form': bound_form,
			'user': request.user
		}
		return render(request, self.template, context=context)


class TaskUpdate(LoginRequiredMixin, View):
	model = Task
	model_form = TaskTextForm
	template = 'board/task_update.html'
	page = 'board:index'
	raise_exception = True

	def get(self, request, pk):
		lst = self.model.objects.filter(user_id=request.user)
		obj = get_object_or_404(lst, pk=pk)
		bound_form = self.model_form(instance=obj)
		context={
			'tasks_todo': lst.filter(state='T'),
			'tasks_now': lst.filter(state='P'),
			'tasks_done': lst.filter(state='D'),
			'task': obj,
			'form': bound_form,
			'user': request.user
		}
		return render(request, self.template, context=context)

	def post(self, request, pk):
		lst = self.model.objects.filter(user_id=request.user)
		obj = get_object_or_404(lst, pk=pk)
		bound_form = self.model_form(request.POST, instance=obj)
		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(reverse(self.page))
		context={
			'tasks_todo': lst.filter(state='T'),
			'tasks_now': lst.filter(state='P'),
			'tasks_done': lst.filter(state='D'),
			'task': obj,
			'form': bound_form,
			'user': request.user
		}
		return render(request, self.template, context=context)


class TaskDelete(LoginRequiredMixin, View):
	model = Task
	page = 'board:index'
	raise_exception = True

	def post(self, request, pk):
		obj = get_object_or_404(self.model, pk=pk, user_id=request.user)
		obj.delete()
		return redirect(reverse(self.page))


class TaskLeave(ChangeStateMixin):
	state = "T"


class TaskProcess(ChangeStateMixin):
	state = "P"


class TaskDone(ChangeStateMixin):
	state = "D"


class CustomLoginView(auth_views.LoginView):
	template_name='board/login.html'


class CustomLogoutView(auth_views.LogoutView):
	next_page='board:login'
