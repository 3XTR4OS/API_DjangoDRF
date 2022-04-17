from django.db import models
from django.core.validators import RegexValidator
import timezone_field
import pytz


class Mailing(models.Model):
    start_date_and_time = models.DateTimeField(auto_now_add=True)
    message_text = models.TextField(blank=True)
    client_filter = models.TextField()
    end_date_and_time = models.DateTimeField()


class Client(models.Model):
    phoneNumberRegex = RegexValidator(regex=r"^7\d{10}$")
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=11)
    operator_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=6)


class Message(models.Model):
    send_date_and_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    id_mailing = models.ForeignKey('Mailing', on_delete=models.PROTECT, null=True)
    id_client = models.ForeignKey('Client', on_delete=models.PROTECT, null=True)


class MailingStatistic(models.Model):
    #### SIMPLE STATISTIC ####
    # how many created
    # sended or not
    # count of sended
    # status: (code 400 or ['Message': bbllbl, code: OK]
    #### DETAIL STATISTIC ####
    # конкретная рассылка
    # конкретная детальная статистика отправленных сообщений
    pass
