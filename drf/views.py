from rest_framework.response import Response
from rest_framework.decorators import api_view

from  .serializers import UserSerializer
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['POST'])
def login(request):
    user=get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)
    token, created=Token.objects.get_or_create(user=user)
    serializer=UserSerializer(instance=user)
    return Response({'token':token.key,'user':serializer.data})


@api_view(['POST'])
def signup(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # We need to get the user from the database and give them a token, but before saving the user we must hash the password first
        user=User.objects.get(username=request.data['username'])
        # Then we need to hash the password for security reasons
        user.set_password(request.data['password'])
        user.save()
        # Then provide the token
        token =Token.objects.create(user=user)
        return Response({'token':token.key,'user':serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response('passed for {}'.format(request.user.email))


