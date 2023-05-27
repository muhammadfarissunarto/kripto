from django.urls import path
from .views import UserRegistrationView, RecordListView, RecordCreateView, RecordUpdateView


urlpatterns = [
    path('', RecordListView.as_view(), name='record'),
    path('create/', RecordCreateView.as_view(), name='create'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('update/<int:pk>', RecordUpdateView.as_view(), name='update'),
]