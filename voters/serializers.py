from rest_framework import serializers

from .models import Voters


class VotersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voters
        fields = ['name', 'last_name', 'adress','number_phone', 'number_identification', 'votingbooth_id']
        read_only_fields = ['coordinates', 'created_at', 'user_id_created']
