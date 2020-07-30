from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class HelloApiView(APIView):
    """
    test api view
    """

    serializer_class = serializers.HelloSerializer

    def get(self, request, pattern=None):
        """
        returns list of APIViews features
        """

        api_features = [
            'gives you the most control over your logic',
            'uses http methods as functions',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Your list is ready', 'api_features': api_features})

    def post(self, request):
        """
        returns value of name field
        """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = {'message': name}
            return Response(message)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        use to update data
        """

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        use to partially update data
        """

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        use to delete data
        """

        return Response({'method': 'DELETE'})
