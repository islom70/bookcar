from django.urls import path
from .views import CarDetailView, home, profile

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CarDetailView.as_view(), name='detail'),
    path('profile/', profile, name='profile')
]