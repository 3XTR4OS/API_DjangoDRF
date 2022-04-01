from rest_framework import serializers
from .models import Client, Mailing, Message


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'operator_code', 'tag', 'time_zone')


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = ('id', 'start_date_and_time', 'message_text', 'client_filter', 'end_date_and_time')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'send_date_and_time', 'status', 'id_mailing', 'id_client')
