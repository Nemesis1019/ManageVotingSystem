from rest_framework import serializers

from .models import Votingbooth, Departament, Municipality


class VotingBoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votingbooth
        fields = '__all__'


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = '__all__'


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'


class VotingGet(serializers.ModelSerializer):
    registers = MunicipalitySerializer(
        source='municipality_set', many=True, read_only=True)

    class Meta:
        model = Votingbooth
        fields = ('id', 'name', 'adress', 'registers')
