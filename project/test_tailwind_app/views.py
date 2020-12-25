from django.shortcuts import render

def index(request):
	text = "Hello World"
	context = {
		'text' : text,
	}
	return render(request, 'test_tailwind_app/index.html', context)