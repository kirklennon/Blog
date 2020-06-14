from photos.models import Post, Location
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

def index(request):
	all_posts = Post.objects.all()
	locations = Location.objects.all()
	paginator = Paginator(all_posts, 10)
	page_number = request.GET.get('page')
	posts = paginator.get_page(page_number)
	context = {
		'locations': locations,
		'posts': posts,
	}
	return render(request, 'index.html', context=context)

def PostDetailView(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'view_post.html', {'post':post})

def LocationDetailView(request, slug):
	location = get_object_or_404(Location, slug=slug)
	
	paginator = Paginator(Post.objects.filter(location=location), 10)
	page_number = request.GET.get('page')
	posts = paginator.get_page(page_number)
	context = {
		'location': location,
		'posts': posts,
	}
	return render(request, 'view_location.html', context=context)