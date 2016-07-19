from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    """
    Our First REST API for GET Requests
    """

    def get(self, request, format=None):
        return Response({'detail': "Hello REST World"})


# Create your views here.
