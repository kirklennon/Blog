from django.db import models 
from django.urls import reverse
from django.contrib import admin
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField(null=True, blank=True)
	posted = models.DateField(db_index=True, auto_now_add=True)
	location = models.ForeignKey('photos.Location', on_delete=models.CASCADE)
	
	image = models.ImageField(upload_to='photos/', null=True, blank=True)
	image_thumbnail = ImageSpecField(source='image',
									  processors=[Thumbnail(520, 520)],
									  format='JPEG',
									  options={'quality': 60})
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