from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', UpdateTodo.as_view()),
    # path('get/', get),
    # path('get/<int:id>', get),
    path('', ListTodo.as_view()),
    path('create/', CreateTodo.as_view()),
    path('delete/', delete),

]