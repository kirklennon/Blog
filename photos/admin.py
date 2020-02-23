from django.contrib import admin
from photos.models import Blog, Location, Image


admin.site.register(Location)

class InlineImage(admin.TabularInline):
	model = Image

class BlogAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

admin.site.register(Blog,BlogAdmin)