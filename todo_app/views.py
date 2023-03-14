from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import ToDoSerializer


@api_view(['GET'])
def get_todos(request: Request):
    queryset = Todo.objects.all()
    # SELECT * FROM todo -> QuerySet([{title..., desc...}])
    print(queryset)
    serializer = ToDoSerializer(queryset, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_todo(request: Request) -> Response:
    serializer = ToDoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    todo = Todo.objects.create(**serializer.data)
    todo.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    # if serializer.is_valid():
    #     todo = Todo.objects.create(**serializer.data)
    #     todo.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)