from rest_framework import serializers
from .models import User
import keys,messages

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('mobile', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            mobile=validated_data['mobile']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializers(serializers.ModelSerializer):
    """ SERIALIZER FOR VERIFYING USER """
    mobile = serializers.CharField(max_length=10,write_only=True, required=True,error_messages={keys.MAX_LENGTH: messages.ENSURE_10_CHAR,keys.REQUIRED:messages.MOBILE_REQUIRED,keys.BLANK:messages.MOBILE_REQUIRED})
    password = serializers.CharField(max_length=10,read_only=True,error_messages={keys.MAX_LENGTH: messages.ENSURE_10_CHAR,})
    class Meta:
        model = User
        fields = ['mobile','password',]