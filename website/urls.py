from django.urls import path, include
from .views import UserRegistrationView, RecordListView, RecordCreateView


urlpatterns = [
    path('', RecordListView.as_view(), name='record'),
    path('create/', RecordCreateView.as_view(), name='create'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]