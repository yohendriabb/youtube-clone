from django.shortcuts import render, redirect
from post.models import Post
from post.forms import PostForm
from .models import Profile

def index(request):
	posts = Post.objects.all()
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user 
			post.save()
			return redirect('index')
	else:
		form = PostForm()
	data= {
	'post':posts,
	'form':form
	}
	return render(request, 'index.html', data)
