# Blog

This is a simple photo blog created using Django. Each post has one photo with an optional description and is tagged with a location (country). The posts are created using the Admin interface and it uses [ImageKit](https://pypi.org/project/django-imagekit) (which uses [Pillow](http://pypi.python.org/pypi/Pillow)) to automatically generate thubmails.

## Unfinished

* You can view by location but it currently just shows a bulleted list organized by post name rather than the name, description, and thumbnail.
* The index view is currently limited to ten posts but it needs pagination added.
* The location view needs the numerical limit and pagination added too.
* I need to tweak the thumbnail code to generate higher (Retina) quality images.
