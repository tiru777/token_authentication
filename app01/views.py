from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    def get(self, request):
        permission_classes = (IsAuthenticated,)
        content = {'message': 'Hello, World!'}
        return Response(content)
