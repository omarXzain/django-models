from django.urls import path, include
from .views import HomeView, PostDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', PostDetailsView.as_view(), name='snack_details')
]
