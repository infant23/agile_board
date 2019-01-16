from django.shortcuts import redirect


def redirect_board(request):
	return redirect('board:index', permanent=True)
