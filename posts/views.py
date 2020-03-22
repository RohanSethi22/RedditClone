from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
import datetime

# Create your views here.
def home(request):
	posts=Post.objects.order_by('-votes','-pdate')
	return render(request, 'posts/home.html', {'posts':posts})

@login_required
def create(request):
	message=''
	if request.method=='POST':
		if request.POST['title']!='' and request.POST['link']!='':
			if request.POST['link'].startswith('http://') or request.POST['link'].startswith('https://'):
				plink=request.POST['link']
			else:
				plink='http://'+request.POST['link']
			Post.objects.create(title=request.POST['title'], link=plink, votes=1, author=request.user, pdate=datetime.datetime.now())
			message='Post added.'
		else:
			message='Title and link must be provided.'
		#return redirect('home')
		return render(request, 'posts/create.html', { 'message': message } )
	else:
		return render(request, 'posts/create.html', { 'message': message } )

@login_required
def upvote(request, postid):
	if request.method=='POST':
		cur_post=Post.objects.get(id=postid)
		cur_post.votes+=1
		cur_post.save()
	else:
		pass
	return redirect('home')

@login_required
def downvote(request, postid):
	if request.method=='POST':
		cur_post=Post.objects.get(id=postid)
		cur_post.votes-=1
		cur_post.save()
	else:
		pass
	return redirect('home')

def userposts(request, puser):
	posts=Post.objects.order_by('-votes','-pdate').filter(author=puser)
	return render(request, 'users/userposts.html', {'posts':posts})