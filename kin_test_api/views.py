from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from users.models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User

class UserProfileView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.filter()
    serializer_class = ProfileSerializer

    def get(self, request,):
        profile = get_object_or_404(Profile, pk=request.user.pk)
        data = ProfileSerializer(profile).data
        return Response(data)

@api_view(['PATCH'])
def user_profile_update(request):
    if request.method == 'PATCH':
        serializer = ProfileSerializer(request.user.profile, data=request.data)

        if serializer.is_valid():
            print('valid')
            profile = serializer.save()
            return Response(ProfileSerializer(profile).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
