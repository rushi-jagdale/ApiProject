
from django.urls import  path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from Apiapp.views import RegistrationAPIView,AdvisorViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
   
    #path('api/v1/auth/auth-token', obtain_auth_token, name='obtain-auth-token')
    path('auth/register/',views.RegistrationAPIView.as_view(), name='register'),
    path('admin/advisor/',views.AdvisorViewSet.as_view(), name='advisor'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),

]