from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django import forms
from .forms import PostForm


from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def Login(request):
	next = request.GET.get('next', '/post_list/')
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)

	if user is not None:
		if user.is_active:
			login(request. user)
			return HttpResponseRedirect(next)
		else:
			return HttpResponse("Inactive user.")
	else:
		return HttpResponseRedirect(settings.LOGIN_URL)

	return render(request, 'login.html', {'redirect_to': next})

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'testapp/post_list.html', {'posts': posts})




def Home(request):
	return render(render, "testapp/post_list.html")

class TestView(APIView):
    """
    Our First REST API for GET Requests
    """

    def get(self, request, format=None):
        return Response({'detail': "This is a test REST Api"})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'testapp/post_detail.html', {'post':post})


@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('testapp.views.post_detail', pk = post.pk)
	else:
		form = PostForm()
		return render(request, 'testapp/post_edit.html', {'form': form})

#@login_required
#def post_edit(request, pk):
	#post = get_object_or_404(Post, pk=pk)
	#return render(request, 'testapp/post_detail.html', {'post':post})

