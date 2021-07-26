from django.conf import settings
from rest_framework import exceptions
from rest_framework.response import Response
from minhascontas.authentication.serializers import TokenUserSerializer, UserPostSerializer, UserSerializer
from minhascontas.authentication.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
import jwt


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = UserPostSerializer
        return serializer_class

class TokenIsValidViewSet(APIView):
    def get(self, request):
        return Response(request.data)

    def post(self, request, *args, **kwargs):
        try:
            token = request.data["access"]
            decode = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except jwt.InvalidSignatureError:
            raise exceptions.AuthenticationFailed('access_token invalid token')
        except KeyError:
            raise exceptions.AuthenticationFailed('access_token invalid key')
        user = User.objects.filter(id=decode["user_id"]).values()[0]
        user = TokenUserSerializer(User.objects.filter(id=decode["user_id"]).values()[0])
        decode.update(user.data)
        return Response(decode)
