from rest_framework import serializers
from app_auth.models import forumUser
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = forumUser
        fields = ('id', 'username', 'email', 'password', 'repeated_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        pw = self.validated_data['password']
        rpw = self.validated_data['repeated_password']
        if pw != rpw:
            raise serializers.ValidationError({"password": "Passwords must match."})
        
        account = forumUser(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        account.set_password(pw)
        account.save()
        return account
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = forumUser
        fields = ('email', 'password')
        # extra_kwargs to ensure password is write-only (password already default value of forumUser(User))
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if not user or not user.is_active:
                raise serializers.ValidationError("Invalid credentials or inactive user.")
            data['user'] = user
            return data
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")