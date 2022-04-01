from django.contrib import admin
from django.urls import path
from .views import ClientAPIview, MailingAPIview, MessageAPIview, ClientAPIDetailView

urlpatterns = [
    path('clientlist/', ClientAPIview.as_view()),
    path('clientlistdetail/<int:pk>/', ClientAPIDetailView.as_view()),
    path('mailinglist/', MailingAPIview.as_view()),
    path('mailinglistdetail/<int:pk>/', MailingAPIview.as_view()),
    path('messagelist/', MessageAPIview.as_view()),
    path('messagelistdetail/<int:pk>/', MessageAPIview.as_view()),
]
