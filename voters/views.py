from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView

from users.models import User
from .models import Voters
from login.permissions import IsLider
from .serializers import VotersSerializer


class VotersListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'LIDER':
            voters = Voters.objects.filter(user_id_created=request.user)
        else:
            voters = Voters.objects.all()
        serializer = VotersSerializer(voters, many=True)
        return Response(serializer.data)


class VotersCreateView(APIView):

    permission_classes = [IsAuthenticated,IsLider]

    def post(self, request):
        serializer = VotersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id_created=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VotersUpdateView(APIView):
    permission_classes = [IsAuthenticated,IsLider]

    def get_object(self, pk):
        try:
            return Voters.objects.get(pk=pk)
        except Voters.DoesNotExist:
            raise Response()

    def put(self, request, pk):
        voter = self.get_object(pk)
        if request.user.role == 'LIDER' and voter.user_id_created != request.user:
            return Response({"error": "You are not authorized to update this information."}, status=status.HTTP_403_FORBIDDEN)
        serializer = VotersSerializer(voter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VotersTotal(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id_created):
        try:
            user = User.objects.get(pk=user_id_created)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        voter_count = Voters.objects.filter(user_id_created=user).count()
        return Response({ "voter_count_total_system": voter_count}, status=status.HTTP_200_OK)

class VotersTotalforLider(APIView):
    permission_classes = [IsAuthenticated,IsLider]
    def get(self, request, user_id_created):
        if request.user.role == "LIDER" and request.user.id != user_id_created:
            return Response({"error": "You are not authorized to view this information."}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = User.objects.get(pk=user_id_created)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        voter_count = Voters.objects.filter(user_id_created=user).count()
        return Response({"id_user": user_id_created, "voter_count": voter_count}, status=status.HTTP_200_OK)

class VotersDeleteView(APIView):
    permission_classes = [IsAuthenticated,IsLider]

    def get_object(self, pk):
        try:
            return Voters.objects.get(pk=pk)
        except Voters.DoesNotExist:
            raise Response({"error": "Voter not found"},status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        voter = self.get_object(pk)
        if request.user.role == "LIDER" and voter.user_id_created != request.user:
            return Response({"error": "You are not authorized to delete this information."}, status=status.HTTP_403_FORBIDDEN)
        voter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
