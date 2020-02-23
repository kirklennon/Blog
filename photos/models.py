from django.db import models 
from django.urls import reverse
from django.contrib import admin

class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	location = models.ForeignKey('photos.Location', on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog_post_detail', args=(self.slug,))
	
class Location(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog_location_detail', args=(self.slug,))

class Image(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='photos/')