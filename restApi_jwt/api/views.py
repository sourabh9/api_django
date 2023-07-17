from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serializers import CompanySerializers,LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


class login(APIView):

    def post(self,request):
        try:
            data = request.data
            serializer = LoginSerializer(data = data)
            if(serializer.is_valid()):
                name = serializer.data['name']
                password = serializer.data['password']
                print(name,password)
                user = authenticate(username = name,password = password)
                if user is None:
                    return Response({
                        'status':400,
                        'message':'User is not valid'
                    })
                refresh = RefreshToken.for_user(user)
                return Response({
                    'status':200,
                    'refresh':str(refresh),
                    'access':str(refresh.access_token),
                })
        except Exception as ex:
            print(str(ex))
            return Response({
                'status':400,
                "message":""
            })
