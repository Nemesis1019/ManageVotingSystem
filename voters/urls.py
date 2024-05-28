from django.urls import path

from .views import VotersTotal,VotersListView,VotersCreateView,VotersUpdateView,VotersDeleteView,VotersTotalforLider

urlpatterns = [
    path('voters/', VotersCreateView.as_view(), name='register-voter'),
    path('voters/list',VotersListView.as_view(),name='list-voters'),
    path('voters/count/<int:user_id_created>/',VotersTotal.as_view(),name='count-voter'),
    path('voters/count/lider/<int:user_id_created>/',VotersTotalforLider.as_view(),name='count-voter'),
    path('voters/update/<int:pk>/', VotersUpdateView.as_view(), name='voters-update'),
    path('voters/delete/<int:pk>/', VotersDeleteView.as_view(), name='voters-delete'),
    
]