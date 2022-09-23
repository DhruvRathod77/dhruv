from urllib import response
import json
from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializer import *
from todo_app import serializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated]) 
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializer
    filter_backends =[SearchFilter]
    search_fields = ['title','category', 'due_date']

# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated]) 
class UpdateTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializer


# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated]) 
class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializer

# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated]) 
@api_view(['DELETE'])
def delete(request):
    data = {}
    del_id = json.loads(request.body.decode('utf-8'))

    if "id" not in del_id:
        data["success"] = False
        data["msg"] = "Record ID not provided"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    try:
        todo = Todo.objects.filter(id__in=del_id["id"])
    except Todo.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "DELETE":
        result = todo.update(deleted=1)
        data["success"] = True
        data["msg"] = "Data deleted successfully."
        data["deleted"] = result
        return Response(data=data, status=status.HTTP_200_OK)


