from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """
    test api view
    """

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
