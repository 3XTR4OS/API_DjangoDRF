from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Client, Mailing, Message
import requests


@receiver(post_save, sender=Mailing)
def my_callback(created, **kwargs):
    """creating Message object in db and send API request"""
    if created:
        instance = kwargs['instance']
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzkyMzIzOTcsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6I' \
                 'kVYVFJBT1MifQ.Od2PkseQ2s-Q2rI_1cV2UvVIvpcLsG8QmkcKdKapAzU'  # bearer token
        hed = {'Authorization': 'Bearer ' + token}
        URL = 'https://probe.fbrq.cloud/v1/send/'  # Base API url
        # start making message obj
        for client in Client.objects.filter(tag=f"{instance.client_filter}"):
            message = Message(status='waiting', id_mailing=instance, id_client=client)
            # response to
            data = {'id': message.id,
                    'phone': message.id_client.phone_number,
                    'text': message.id_mailing.message_text}
            resp_url = URL + str(data['id'])
            response = requests.post(resp_url, json=data, headers=hed)
            # add state into message
            if response.status_code != 400:
                message.status = response.status_code
            else:
                message.status = 'ОК'
            # end making message obj
            message.save()
