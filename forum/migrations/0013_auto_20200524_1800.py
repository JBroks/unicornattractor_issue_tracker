# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-24 18:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_postvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_thread_key', to='forum.Thread'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_author_key', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postvote',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_vote_post_key', to='forum.Post'),
        ),
        migrations.AlterField(
            model_name='postvote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_vote_author_key', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thread',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread_author_key', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='threadvote',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread_vote_thread_key', to='forum.Thread'),
        ),
        migrations.AlterField(
            model_name='threadvote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread_vote_author_key', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
        migrations.AlterModelTable(
            name='postvote',
            table='post_vote',
        ),
        migrations.AlterModelTable(
            name='thread',
            table='thread',
        ),
        migrations.AlterModelTable(
            name='threadvote',
            table='thread_vote',
        ),
    ]