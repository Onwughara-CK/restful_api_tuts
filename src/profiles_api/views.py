from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


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


class HelloViewset(viewsets.ViewSet):
    """
    use to test API ViewSet
    """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """
        returns a list of Viewset features
        """

        view_features = [
            'more functionalities with less code',
            'less control over code logic',
            'use for basic api calls',
            'has the following actions as methods : [list,create,retrieve,update,partial_update]'
        ]

        return Response({'message': 'hello', "view_features": view_features})

    def create(self, request):
        """
        returns a hello message
        """

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = {'message': 'hello', 'method': 'POST'}
            return Response(message)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        returns a message
        """

        return Response({'message': 'GET'})

    def update(self, request, pk=None):
        """
        returns a message
        """

        return Response({'message': 'PUT'})

    def partial_update(self, request, pk=None):
        """
        returns a message
        """

        return Response({'message': 'PATCH'})

    def destroy(self, request, pk=None):
        """
        deletes a message
        """

        return Response({'message': 'DESTROY'})
