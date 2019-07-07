from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handle creating, reading, updating actions for profile feed item"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""

        serializer.save(user_profile=self.request.user)





class UserLoginApiView(ObtainAuthToken):
    """creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)  

class HelloViewset(viewsets.ViewSet):
    """test api viewset"""

    serializer_class = serializers.HelloSerializer

  
    def list(self, request):
        """return a hello message"""

        a_viewset = ['uses actions (create, list, retrieve, update, partial_update', 'provides more functionality with less code']




        return Response({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            return Response({'message': f'Hello {name}'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object by replacing whole object with new one"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handle removing an object"""

        return Response({'http_method': 'DELETE'})







class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of api view features"""
        an_apiview = ['Uses http methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional Django view', 'Gives you the most control over application logic',
        'is mapped manually to urls']

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object by replacing object"""

      
        return Response({'method': 'PUT'})
     


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""

        serializer = self.serializer_class(data=request.data)

        return Response({'method': 'PATCH'})

    

    def delete(self, request, pk=None):
        """Delete object from db"""
        return Response({'method': 'DELETE'})
        
