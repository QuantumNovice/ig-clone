from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
# Create your views here.


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GenerateTokenView(APIView):
    permission_classes = (IsAuthenticated,)  

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST', 'GET'])
def login(request):
    """
    List all code snippets, or create a new snippet.
    """
    """
    {
    "name":"S",
    "email":"S",
    "password":"S"
    }

    Returns:
        _type_: _description_
    """
    print('login api_view')
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            print(request.data)
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"login":True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)