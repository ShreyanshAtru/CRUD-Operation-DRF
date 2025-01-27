from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import TaskSerializer, RegisterSerializer, UserSerializer
from .models import Task
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "list": "/task/-list",
        "create": "/task-create",
    }
    return Response(api_urls)


@api_view(["GET"])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def taskdetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def taskupdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def taskdelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response("Succesfully deleted!!")


class UserRegistrationView(generics.GenericAPIView):
    """
    view for registering a new user
    returning a dict of registered user details
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # print(100*"*", serializer)
        if serializer.is_valid(raise_exception=True):
            if (
                serializer.validated_data["password"]
                != serializer.validated_data["password_confirmation"]
            ):
                return Response(
                    {"error": "passowrd do not match"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            # user = serializer.save()  we can also use this to create the user

            user = User.objects.create_user(
                username=serializer.validated_data["username"],
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )
            return Response(
                {
                    "user": UserSerializer(
                        user, context=self.get_serializer_context()
                    ).data,
                    # we can skip above two lines but we're using this to show the field of User data
                    "message": "User Created Successfully.  Now perform Login to get your token",
                }
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
