from django.db import models


class Tag(models.Model):
	name = models.CharField(max_length=240)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to='category_image', null=True, blank=True)

	def __str__(self):
		return self.name	
		
class Post (models.Model):
	name = models.CharField(max_length=64)
	title = models.CharField(max_length=255)
	body = models.TextField()
	publish_date = models.DateField(auto_now_add=True)
	updated_date = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to='post_images/', null=True, blank=True)
	tags = models.ManyToManyField(Tag)
	categorys = models.ManyToManyField(Category)
	

	def __str__(self):
		return self.title


class PostImage(models.Model):
	post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='post_gallery', null=True, blank=True)		