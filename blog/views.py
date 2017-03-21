from django.shortcuts import redirect,render_to_response
from .models import Post
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .forms import PostForm,ContactForm
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext,Context
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def post_list(request):
	posts =	Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
	
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})
   
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def search_q(request):
	if 'q' in request.GET and request.GET['q']:
		q=request.GET['q']
		posts=Post.objects.filter(title__icontains=q)
		return render(request,'blog/search.html',
		{'books':books,'query':q})
	else:
		return HttpResponse("Please submit a search term.")	
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            topic=form.cleaned_data['topic']
            message=form.cleaned_data['message']
            sender=form.cleaned_data.get('sender','jprrahultiwari@gmail.com')
            send_mail(
            'Feedback from your site,topic:%s'%topic,
            message,sender,
            ['jprrahultiwari@gmail.com']
            )
            return render(request,'blog/thanks.html')
    else:
        form=ContactForm()

    context={'form':form}
    return render(request,'blog/contact.html',context)