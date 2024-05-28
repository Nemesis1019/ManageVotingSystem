from django.urls import path

from .views import VotingboothCreateAPIView,VotingList,VotsforVotingBooth,Votsformunicipality

urlpatterns = [
    path('voting/', VotingboothCreateAPIView.as_view(), name='register-votingbooth'),
    path('voting/list/', VotingList.as_view(), name='list-votingbooth'),
    path('votingbooth/<int:votingbooth_id>/voters/', VotsforVotingBooth.as_view(), name='vots-for-votingbooth'),
    path('municipality/<int:municipality_id>/voters/',Votsformunicipality.as_view(),name='vots-for-municipality')
]