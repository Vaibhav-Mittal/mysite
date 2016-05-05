from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, Category

# Create your views here.
def index(request):
	return render_to_response('blog/index.html',{})
	
def view_post(request, slug):
	return render_to_response('blog/view_post.html',
	{
	'post':get_object_or_404(Blog, slug=slug)
	}
	)
	
def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('blog/view_category.html',
	{
	'category':category,
	'posts':Blog.objects.filter(category=category)[:5]
	}
	)
	
