from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        required = True,
        style = {"inpyt_type": "password"}
    )
    password_confirm = serializers.CharField(
        write_only = True,
        required = True,
        style = {"inpyt_type": "password"}
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirm', 'is_active', 'payment_verified')
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs["password_confirm"]:
            raise serializers.ValidationError({
                "password": "Las contraseñas no coinciden"
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        # usare Type ignore solo para ignorar el warning que me da pyright en el ide de zed no afecta al codigo ni a lo demas
        return User.objects.create_user(**validated_data) # type: ignore

    def to_representation(self, instance):
        data = super().to_representation(instance)

        refresh = RefreshToken.for_user(instance)

        data['tokens'] = {
            'refres': str(refresh),
            'access': str(refresh.access_token)
        }

        return data

class LoginSerializer(serializers.Serializer):
    pass
