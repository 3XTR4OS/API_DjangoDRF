import json
import subprocess
from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import render
import requests
import time
from .models import Client, Mailing, Message
from .serializers import ClientSerializer, MailingSerializer, MessageSerializer


def mail_sender(request):
    # print('-' * 50)
    # print(Message.objects.get(id=5))
    # print(Client.objects.get(id=17).phone_number)
    # print(Mailing.objects.get(id=30).message_text)
    # print('-' * 50)
    return HttpResponse("Hello, world. You're at the polls index.")
    # print([i.phone_number for i in Client.objects.filter(tag="all")])
    # print([i.message_text for i in Mailing.objects.all() if i.client_filter in [i.tag for i in Client.objects.filter(tag='MTS')]])
    # while True:
    #     responses = []
    #     token = auth_token.auth_token()
    #     hed = {'Authorization': 'Bearer ' + token}
    #     url = 'https://probe.fbrq.cloud/v1/send/'
    #     responses = []
    #
    #     for item in Client.objects.all():
    #         data = {'id': item.id, 'phone': item.phone_number, 'text': 'привет мир'}
    #         resp_url = url + str(data['id'])
    #         response = requests.post(resp_url, json=data, headers=hed)
    #         responses.append(response)
    #
    #         # # Добавлено для теста ошибок. (!!!ПОТОМ УДАЛИТЬ!!!)
    #         # response = requests.post(resp_url, json=data)
    #         # responses.append(response)
    #         #
    #         # # Добавлено для теста ошибок. (!!!ПОТОМ УДАЛИТЬ!!!)
    #         # response = requests.post(url)
    #         # responses.append(response)
    #         #
    #         # # Добавлено для теста ошибок. (!!!ПОТОМ УДАЛИТЬ!!!)
    #         # response = requests.post(url + str('1'))
    #         # responses.append(response)
    #         # print(data)
    #         print(response)
    #         print([i.text for i in responses])
    #     time.sleep(10)


#
# def redir_to_mail_sender(request):  # отправляет и отображает результат запросов к стороннему API
#     subprocess.Popen(mail_sender())
#     return HttpResponse("Рассылки запущены")
#     # dates = [i.start_date_and_time for i in Mailing.objects.all()]
#
#     # responses = []
#     #
#     # for item in Client.objects.all():
#     #     data = {'id': item.id, 'phone': item.phone_number, 'text': 'привет мир'}
#     #     resp_url = url + str(data['id'])
#     #     response = requests.post(resp_url, json=data, headers=hed)
#     #     responses.append(response)
#     #
#     #     # # Добавлено для теста ошибок. (!!!ПОТОМ УДАЛИТЬ!!!)
#     #     # response = requests.post(resp_url, json=data)
#     #     # responses.append(response)
#     #     #
#     #     # # Добавлено для теста ошибок. (!!!ПОТОМ УДАЛИТЬ!!!)
#     #     # response = requests.post(url)
#     #     # responses.append(response)
#     #     #
#     #     # # Добавлено для теста ошибок. (!!!ПОТОМ УДАЛИТЬ!!!)
#     #     # response = requests.post(url + str('1'))
#     #     # responses.append(response)
#     #     # print(data)
#     #     # print(response)
#     #     # print(responses)
#     # print('-' * 50)
#     # print(dates)
#     # print('-' * 50)
#     # return render(request, 'index.html', context={'responses': responses})


class ClientAPIview(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingAPIview(generics.ListCreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MailingAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MessageAPIview(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
