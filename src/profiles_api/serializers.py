from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """
    Use to serialize name field to test HelloApiView
    """
    name = serializers.CharField(max_length=10)
