from django.contrib.auth import get_user_model, login, logout, authenticate
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.authtoken.models import Token
from .serializers import Win_One_Serializer, LoginSerializer,UserRegisterSerializer
from Wing.models import Wing_One
from .validations import custom_validation


class UserRegisterApi(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginApi(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
            'status':False,
            'data': serializer.errors
		})
        username = serializer.data['username']
        password = serializer.data['password']
        
        user_obj = authenticate(username=username, password=password)
        if user_obj:
            token , _ = Token.objects.get_or_create(user=user_obj)
            return Response({
				'status':True,
                'Token':token.key
		})
        

        return Response({
            'status':False,
            'data': {},
            'message':'Invalid Credentials'
		})



class Wing_One_API_View(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = Win_One_Serializer
    queryset = Wing_One.objects.all()


class Wing_One_Create_API_View(generics.CreateAPIView):
    serializer_class = Win_One_Serializer
    queryset = Wing_One.objects.all()

