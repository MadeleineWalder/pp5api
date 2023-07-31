from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from pp5api.permissions import IsOwnerOrReadOnly


class ProfileList(APIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many=True, context={'request': request}
        )
        return Response(serializer.data)


class ProfileDetail(APIView):
    # fetch profile by ID if it exists
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            # if user does NOT own profile will throw 403 Forbidden error
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    # call serializer with the profile and request data
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, context={'request': request}
        )
        return Response(serializer.data)

    # if data is valid save and return instance, if invalid return 400
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
