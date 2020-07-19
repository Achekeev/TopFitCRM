from django.contrib import admin
from django.urls import path
from .views import ClientsListView, ClientDetailView, TrainersListView, TrainersDetailView

urlpatterns = [
    path('client_list/', ClientsListView.as_view(), name='client-list'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('trainer_list/', TrainersListView.as_view(), name='trainer-list'),
    path('trainer_detail/<int:pk>/', TrainersDetailView.as_view(), name='trainer-detail')
]
