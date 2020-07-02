# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-07-01 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvote',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upvote_ticket_key', to='tickets.Ticket'),
        ),
    ]
