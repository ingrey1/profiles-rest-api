from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of api view features"""
        an_apiview = ['Uses http methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional Django view', 'Gives you the most control over application logic',
        'is mapped manually to urls']

        return Response({'message': 'Hello', 'an_apiview': an_apiview})