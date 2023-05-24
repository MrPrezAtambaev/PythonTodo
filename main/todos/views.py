from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoItemSerializer, AuthSerializer, LoginSerializer
from .models import TodoItem
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @api_view(['POST'])
    def update_items(request, pk):
        item = TodoItem.objects.get(pk=pk)
        data = TodoItemSerializer(instance=item, data=request.data)

        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['Delete'])
    def delete_items(request, pk):
        item = TodoItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = AuthSerializer

    @api_view(['POST'])
    def register(request):
        data = AuthSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LoginViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = LoginSerializer

    @api_view(['POST'])
    def login(self, request):
        data = LoginSerializer(data=request.data)
        if data.is_valid():
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
