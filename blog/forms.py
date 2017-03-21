from django import forms
from .models import Post
TOPIC_CHOICES=(
('general','General enquiry'),
('bug','Bug report'),
('suggestion','Suggestion'),
)

class PostForm(forms.ModelForm):
	class Meta:
		model =Post
		fields=('title','text',)
class ContactForm(forms.Form):
	topic=forms.ChoiceField(choices=TOPIC_CHOICES)
	message=forms.CharField(max_length=50)
	sender=forms.EmailField(required=True)
