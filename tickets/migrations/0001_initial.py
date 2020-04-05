# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-05 12:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], max_length=7)),
                ('ticket_status', models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Closed', 'Closed')], max_length=11)),
                ('subject', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=3000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
