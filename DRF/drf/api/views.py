from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializer import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list':'/task/-list',
        'create':'/task-create',
    }
    return Response(api_urls)


@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskdetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskupdate(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks,many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskdelete(request,pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response("Succesfully deleted!!")