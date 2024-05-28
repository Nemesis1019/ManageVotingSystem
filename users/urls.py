from django.urls import path

from .views import AdminRegistrationView,LiderRegistrationView,UserLoginView,LogoutView


urlpatterns = [
    path('register/admin/', AdminRegistrationView.as_view(), name='register-admin'),
    path('register/lider/', LiderRegistrationView.as_view(), name='register-lider'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]