from photos.models import Blog, Location
from django.shortcuts import render, get_object_or_404

def index(request):
	locations = Location.objects.all()
	posts = Blog.objects.all()[:5]
	context = {
		'locations': locations,
		'posts': posts
	}
	return render(request, 'index.html', context=context)

def BlogDetailView(request, slug):
	post = get_object_or_404(Blog, slug=slug)
	return render(request, 'view_post.html', {'post':post})

def LocationDetailView(request, slug):
	location = get_object_or_404(Location, slug=slug)
	posts = Blog.objects.filter(location=location)[:5]
	context = {
		'location': location,
		'posts': posts}
	return render(request, 'view_location.html', context=context)