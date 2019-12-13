from django.shortcuts import render

from django.http import HttpResponse


posts = [
    {
    'author': 'pavan',
    'title': 'nobody',
    'content': 'my wish',
    'date_posted': 'august 27'
    },
    {
    'author': 'kumar',
    'title': 'no',
    'content': 'wish',
    'date_posted': 'august 28'
    }
]

def home(request):
	context = {
	'posts': posts,
	 'title': 'power'
	}
	return render(request, 'blog/home.html',context)


def about(request):
	return render(request, 'blog/about.html')

# Create your views here.
