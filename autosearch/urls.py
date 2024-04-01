from django.urls import path

from . import views

urlpatterns = [
	path('get-names/', views.get_names, name = "get_names"),
	path('', views.index, name="index"),
]