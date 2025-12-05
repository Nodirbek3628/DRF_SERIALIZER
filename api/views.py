from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from .serializer import CategorySerializer,TaskSerializer,RegisterSerializer,LoginSerializer
from .models import Category,Task,User


class RegisterAPIView(APIView):

    def post(self,request:Request)->Response:
        serialezr = RegisterSerializer(data=request.data)

        if serialezr.is_valid(raise_exception=True):
            validated_data = serialezr.validated_data

            username = validated_data['username']

            try:
                User.objects.get(username = username)
                return Response({'errors':'user exists'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                user = User(username=username)
                user.set_password(validated_data['password'])
                user.save()
                return Response()

        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(APIView):
    
    authentication_classes = [TokenAuthentication]

    def post(self,request:Request)->Response:
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user is None:
                return Response({'error':'not found password '},status=status.HTTP_404_NOT_FOUND)
            token, created = Token.objects.get_or_create(user=user)  # Token uchun
            return Response({'token': token.key})
            
        return Response({'sucseefull':'login'},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)



class CategoryViewSet(ModelViewSet):
    serializer_class=CategorySerializer
    queryset = Category.objects.all()


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


