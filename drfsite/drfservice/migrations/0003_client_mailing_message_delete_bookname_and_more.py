# Generated by Django 4.0.3 on 2022-03-20 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfservice', '0002_bookname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=100)),
                ('operator_code', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('time_zone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('message_text', models.TextField(blank=True)),
                ('client_filter', models.TextField()),
                ('end_date_and_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('id_mailing', models.IntegerField()),
                ('id_client', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='BookName',
        ),
        migrations.RemoveField(
            model_name='women',
            name='cat',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Women',
        ),
    ]
