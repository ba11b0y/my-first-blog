from django.db import models
from django.utils import timezone
# Create your models here.
class Author(models.Model):
	name=models.CharField(max_length=30)
	country=models.CharField(max_length=40)
	designation=models.CharField(max_length=40)
	email=models.EmailField()
	def __str__(self):
		return self.name
class Post(models.Model):
	authors=models.ManyToManyField(Author)
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)
	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def __str__(self):
		return self.title
	class Admin:
		list_display=('title','authors')
		search_fields=('title',)
