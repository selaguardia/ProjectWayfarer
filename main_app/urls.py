from django.urls import path
from . import views
from .views import Signup, Home, ProfileDetail, ProfileEdit

urlpatterns = [
    path('accounts/signup/', Signup.as_view(), name='signup'),
    path('', Home.as_view(), name='home'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile'),
    path('profile/<int:pk>/edit', ProfileEdit.as_view(), name='edit')
]
