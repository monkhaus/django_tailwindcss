from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post, Idea
from .forms import CreateBlogForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import requests


class BlogListView(ListView):

	url = "https://text-sentiment.p.rapidapi.com/analyze"

	payload = """text=Anyway I began to feel really guilty 
	pretty soon after. At first I was too afraid to give it back, 
	cause I even helped him look for it and I didn't want to lose him as a friend. So a couple months later, I came up with the idea of just putting it back into his mailbox, which I did."""
	headers = {
	    'content-type': "application/x-www-form-urlencoded",
	    'x-rapidapi-key': "4099d682e6mshac8d2ae4aa4d95ep18037ajsn5c407850c9dd",
	    'x-rapidapi-host': "text-sentiment.p.rapidapi.com"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)
	model = Post
	template_name = 'blog/index.html'

	def get_context_data(self, **kwargs):
		context = super(BlogListView, self).get_context_data(**kwargs)
		context.update({
			'idea_list' : Idea.objects.all(),
			})
		return context

	def get_queryset(self):
		return Post.objects.filter(author=self.request.user)[::-1]

class BlogDetailView(DetailView): # new
	model = Post
	template_name = 'blog/detail.html'


class BlogCreateView(CreateView):

	model = Post
	template_name = 'blog/create.html'
	fields = ['title', 'body']
	
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.author = self.request.user
		obj.save()
		return HttpResponseRedirect(reverse('blog:post_detail', args=[str(obj.id)]))


class BlogUpdateView(UpdateView): # new
	model = Post
	template_name = 'blog/update.html'
	fields = ['title', 'body']


class BlogDeleteView(DeleteView): # new
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('blog:blog_posts')


