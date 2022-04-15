from django.contrib import admin
from django.urls import path
from .views import ClientAPIview, ClientAPIDetailView, MailingAPIview, MailingAPIDetailView, MessageAPIview, \
    MessageAPIDetailView, mail_sender

urlpatterns = [
    path('clients/', ClientAPIview.as_view()),
    path('clients/<int:pk>/', ClientAPIDetailView.as_view()),
    path('mailings/', MailingAPIview.as_view()),
    path('mailings/<int:pk>/', MailingAPIDetailView.as_view()),
    path('messages/', MessageAPIview.as_view()),
    path('messages/<int:pk>/', MessageAPIDetailView.as_view()),
]
