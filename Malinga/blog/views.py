from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

def admin(request):
	return render(request, 'admin/index2.html')

def home(request, ):
	post = Post.objects.all()
	object_list = Post.objects.all().order_by('-publish_date')[:3]
	return render(request, 'index.html', {'posts':post, 'object_lists':object_list})


def blogs(request):
	post = Post.objects.all()
	return render(request, 'blogs.html', {'posts':post})


class BlogView(DetailView):
	model = Post
	template = 'blogpost.html'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def get_context_data(self, pk, *args, **kwargs):
		context = super(FrontPageView, self).get_context_data(**kwargs)
		object_list = Post.objects.all().order_by('-publish_date')[:4]
		
		context.update({
			'object_lists':object_list
			})


def blog(request, pk):
	post = get_object_or_404(Post, pk=pk)
	tag = Tag.objects.filter(post=post)
	category = Category.objects.all()
	categories = Category.objects.filter(post=post)
	#similar_posts = self.object.tags.similar_objects()[:2]
	object_list = Post.objects.all().order_by('-publish_date')[:3]
	context = {'post':post,'categorys':category, 'object_lists':object_list, 'tags':tag,
				'categories':categories}
				#'similar_posts':similar_posts}
	return render(request, 'singleblog.html', context)


def cate(request):
	categorys = Category.objects.all()
	
	context = {'categorys':categorys}
	
	
	return render(request,'categories.html', context)