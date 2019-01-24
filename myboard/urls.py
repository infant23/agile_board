from django.contrib import admin
from django.urls import include, path

from .views import redirect_board


urlpatterns = [
	path('', redirect_board),
	path('board/', include('board.urls')),
    path('admin/', admin.site.urls),
]
