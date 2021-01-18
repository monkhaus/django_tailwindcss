from .models import Post
from django.forms import ModelForm



class CreateBlogForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body']