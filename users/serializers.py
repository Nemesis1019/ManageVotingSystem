from rest_framework import serializers

from .models import Admin, Lider, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        admin = Admin.objects.create(user=user, **validated_data)
        return admin


class LiderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Lider
        fields = ['name','last_name','address','profile_photo','user','number_phone']
        read_only_fields = ['coordinates', 'created_at', 'user_id_created']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        lider = Lider.objects.create(user=user, **validated_data)
        return lider
