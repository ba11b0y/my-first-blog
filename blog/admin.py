from django.contrib import admin
from .models import Post,Author
class AuthorAdmin(admin.ModelAdmin):
	list_display=('name','country','email')
class PostAdmin(admin.ModelAdmin):
	list_display=('title','published_date')	
	list_filter=('authors','published_date')
	search_fields=('title',)
# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Post,PostAdmin)
