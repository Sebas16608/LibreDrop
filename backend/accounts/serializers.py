from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"}
    )
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'password_confirm',
            'is_active',
            'payment_verified'
        )
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
        # El type: ignore funciona perfecto para Zed / Pyright
        return User.objects.create_user(**validated_data) # type: ignore

    def to_representation(self, instance):
        data = super().to_representation(instance)

        refresh = RefreshToken.for_user(instance)

        data['tokens'] = {
            'refresh': str(refresh),  # Corregido: 'refresh'
            'access': str(refresh.access_token)
        }

        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"}
    )

    def validate(self, attrs):
        # Corregido: acceso a diccionarios con .get()
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Corregido: importación de authenticate y uso de self.context
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password,
            )
            if not user:
                raise serializers.ValidationError(
                    "Credenciales inválidas.",
                    code='authorization'
                )
            if not user.is_active:
                raise serializers.ValidationError(
                    "Cuenta desactivada.",
                    code='authorization'
                )
        else:
            raise serializers.ValidationError(
                "Debe incluir username y password.",
                code='authorization'
            )

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        token = RefreshToken.for_user(user)

        return {
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            },
            "tokens": {
                "refresh": str(token),
                "access": str(token.access_token),
            }
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'payment_verified',
            'created_at',
            'updated_at'
        )
        read_only_fields = fields
