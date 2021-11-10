import jwt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import SignInSerializer


class CustomAuthorizationView(APIView):
    """
    View for authorization on jwt token
    """

    @swagger_auto_schema(responses={200: '{"token": string}'}, request_body=SignInSerializer)
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        data = {}
        data['token'] = jwt.encode(
            {'user': user.get_username()},
            'secret', algorithm='HS256'
        )
        return Response(data)


class CustomAuthentication(authentication.BaseAuthentication):
    """
    Authentication on jwt token
    """
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return None

        try:
            data = jwt.decode(
                token, 'secret', algorithms='HS256'
            )
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Invalid token')

        try:
            user = User.objects.get(username=data['user'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
