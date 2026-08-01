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

# TODO: ESTE SERIALIZER ESTÁ INCOMPLETO Y NO SE PUEDE USAR AÚN.
# Los errores conocidos son: campo 'password_confirm' debería ser 'password',
# attrs no es un objeto (usar attrs['username']), falta importar 'authenticate',
# self.context en vez de request.self.context, y el método create está sin terminar.
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password_confirm = serializers.CharField(
        write_only = True,
        required = True,
        style = {"inpyt_type": "password"}
    )

    def validate(self, attrs):
        username = attrs.username
        password = attrs.password

        if username and password:
            user = authenticate(
                request.self.context.get('request'),
                username = username,
                password = password,
            )
            if not user:
                raise serializers.ValidationError("credenciales invalidas", code = 'authorization')
            if not user.is_active:
                raise serializers.ValidationError("Cuenta desacrtivada", code = 'authorization')
        else:
            raise serializers.ValidationError(
                "debe incluir username y password",
                code = 'authorization'
            )
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        token = RefreshToken.for_user

