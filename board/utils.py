from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ChangeStateMixin(LoginRequiredMixin, View):
	model = None
	page = 'board:index'
	raise_exception = True
	state = None

	def post(self, request, pk):
		obj = get_object_or_404(self.model, pk=pk, user_id=request.user)
		obj.state = self.state
		obj.save()
		return redirect(reverse(self.page))
