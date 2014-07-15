from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views import generic
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from myblog.models import Post
from django import forms

class DeleteNewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []

class IndexView(generic.ListView):
    template_name = 'myblog/index.html'
    context_object_name = 'latest_blog_list'
    """
	latest_blog_list = Post.objects.order_by('-pub_date')[:10]
	context = {'latest_blog_list': latest_blog_list}
	return render(request, 'myblog/index.html', context)
	"""

    def get_queryset(self):
        # return last 10 blog posts
        return Post.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:10]

class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            exclude = ['pub_date']

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return HttpResponseRedirect('')
    else:
        form = PostForm()

    return render_to_response('myblog/new.html', {'form': form}, context_instance=RequestContext(request))

def delete(request, id):
    blog = get_object_or_404(Post, pk=id).delete()
    return HttpResponseRedirect(reverse('index'))

def more(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
   # comment = get_object_or_404(Comment, pk=post_id)
   # selected_choice = post.comment_set.get(pk=request.POST['user_comment'])
    return render(request, 'myblog/more.html', {'post': post})

def loginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            print "poularde"
            # Return a 'disabled account' error message
    else:
        print "masay"
        # Return an 'invalid login' error message.
    print HttpResponseRedirect(reverse('auth_login'))
