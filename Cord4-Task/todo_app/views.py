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

class UpdateTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializer

@authentication_classes([JWTAuthentication])     
class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializer

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


# def filtering_query(model, query_string, model_id, classnm):
    # func_name_filter = "ModelFilter" + classnm + "().filter_fields"
    # func_name_search = "ModelFilter" + classnm + "().search"
    # data = {}

    # if "orderBy" not in query_string:
    #     orderby = model_id
    # else:
    #     orderby = str(query_string["orderBy"])

    # if "sortBy" not in query_string:
    #     sortby = ""
    # else:
    #     sortby = str(query_string["sortBy"])
    #     if sortby.lower() == "desc":
    #         sortby = "-"
    #     else:
    #         sortby = ""

    # data["total_record"] = len(model)
    # data["current_page"] = 1

    # if "filter" in query_string:
    #     filter = list(query_string["filter"].split(","))
    #     if filter:
    #         model = eval(func_name_filter + "(model, filter)")
    #         data["total_record"] = len(model)
    # if "search" in query_string:
    #     model = eval(func_name_search + "(model, query_string)")
    #     data["total_record"] = len(model)
    # if orderby:
    #     if sortby:
    #         orderby = sortby + orderby
    #     model = model.order_by(orderby)

    # if len(model) > 0:
    #     model = model.distinct()


    # return model, data

# @api_view(['GET'])
# def get(request, id=None):
#     query_string = request.query_params
#     data={}
#     try:
#         if id:
#             todo = Todo.objects.filter(pk=id, deleted=0)
#         else:
#             todo = Todo.objects.filter(deleted=0)

#         data["total_record"] = len(todo)
#         todo, data = filtering_query(todo, query_string, "id","TODO")

#     except Todo.DoesNotExist:
#         data["success"] = False
#         data["msg"] = "Record Does not exist"
#         data["data"] = []
#         return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

#     if request.method == "GET":
#         serilizer = Todoserializer(todo, many=True)
#         data["success"] = True
#         data["msg"] = "OK"
#         data["data"] = serilizer.data
#         return Response(data=data, status=status.HTTP_200_OK)



# def filtering_query(model, query_string, model_id, classnm):
#     func_name_filter = "ModelFilter" + classnm + "().filter_fields"
#     func_name_search = "ModelFilter" + classnm + "().search"
#     data = {}

#     if "orderBy" not in query_string:
#         orderby = model_id
#     else:
#         orderby = str(query_string["orderBy"])

#     if "sortBy" not in query_string:
#         sortby = ""
#     else:
#         sortby = str(query_string["sortBy"])
#         if sortby.lower() == "desc":
#             sortby = "-"
#         else:
#             sortby = ""

#     data["total_record"] = len(model)
#     data["current_page"] = 1

#     if "filter" in query_string:
#         filter = list(query_string["filter"].split(","))
#         if filter:
#             model = eval(func_name_filter + "(model, filter)")
#             data["total_record"] = len(model)
#     if "search" in query_string:
#         model = eval(func_name_search + "(model, query_string)")
#         data["total_record"] = len(model)
#     if orderby:
#         if sortby:
#             orderby = sortby + orderby
#         model = model.order_by(orderby)

#     if len(model) > 0:
#         model = model.distinct()

#     return model, data


# @api_view(['GET'])
# def get(request, id=None):
#     query_string = request.query_params
#     data={}
#     try:
#         if id:
#             todo = Todo.objects.filter(pk=id, deleted=0)
#         else:
#             todo = Todo.objects.filter(deleted=0)

#         data["total_record"] = len(todo)
#         todo, data = filtering_query(todo, query_string, "category", "TODO")

#     except Todo.DoesNotExist:
#         data["success"] = False
#         data["msg"] = "Record Does not exist"
#         data["data"] = []
#         return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

#     if request.method == "GET":
#         serilizer = Todoserializer(todo, many=True)
#         data["success"] = True
#         data["msg"] = "OK"
#         data["data"] = serilizer.data
#         return Response(data=data, status=status.HTTP_200_OK)
