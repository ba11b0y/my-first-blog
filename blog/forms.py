from django impot forms
from .models import Post
class PostForm(froms.ModelForm):
	class Meta:
	model =Post
	fields=('title','text',)
