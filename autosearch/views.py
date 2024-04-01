from django.shortcuts import render
from .models import Names

from django.http import JsonResponse


def index(request):
	return render(request, 'index.html')


def get_names(request):
	search = request.GET.get("search")
	payload = []
	message = "No match found :("

	if search:
		objs = Names.objects.filter(name__startswith = search)
		for obj in objs:
			payload.append({
				"name": obj.name
			})
		message = f"Total {objs.count()} matches found :)"

	return JsonResponse({
		"status": 200,
		"message": message,
		"payload": payload
	})