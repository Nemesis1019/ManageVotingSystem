from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import VotingBoothSerializer,VotingGet
from .models import Votingbooth
from voters.models import Voters


class VotingboothCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VotingBoothSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VotingList(APIView):
    def get(self, request):
        registros_primer_modelo = Votingbooth.objects.all()
        serializer = VotingGet(registros_primer_modelo, many=True)

        return Response(serializer.data)

class VotsforVotingBooth(APIView):
    def get(self, request, votingbooth_id):
        voters = Voters.objects.filter(votingbooth_id=votingbooth_id)
        total = voters.count()
        
        return Response({'total_voters_for_VotingBooth': total})

class Votsformunicipality(APIView):
    def get(self, request, municipality_id):
        votingbooth = Votingbooth.objects.filter(municipality_id=municipality_id)
        total_voters = 0

        for voter in votingbooth:
            voters_count = Voters.objects.filter(votingbooth_id=voter.id).count()
            total_voters += voters_count

        return Response({
            'total_voters_for_Municipality': total_voters,
        })