from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """
    Use to serialize name field to test HelloApiView
    """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """
    use to serialize model
    """
    class Meta:
        model = models.UserProfile
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        use to create user
        """
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
