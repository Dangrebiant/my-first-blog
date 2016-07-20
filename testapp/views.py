from django.shortcuts import render
from django.utils import timezone
from .models import Post

from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    """
    Our First REST API for GET Requests
    """

    def get(self, request, format=None):
        return Response({'detail': "This is a test REST Api"})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'testapp/post_list.html', {'posts': posts})
