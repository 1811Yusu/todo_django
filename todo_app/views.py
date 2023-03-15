from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import ToDoSerializer, UpdateToDoSerializer


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

@api_view(['PATCH'])
def update_todo(request: Request, pk) -> Response:
    print(pk)
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'detail': f'Todo with {pk} does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UpdateToDoSerializer(instance=todo, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_todo(request: Response, pk) -> Response:
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'detail': f'Todo with {pk} does not exist'}, status=status.HTTP_404_NOT_FOUND)
    todo.delete()
    return Response({'detail': 'Successfully deleted'}, status=status.HTTP_204_NO_CONTENT)

#TODO: Написать функцию для получения одного объекта
#TODO: подключить Swagger