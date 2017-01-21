# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-19 16:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0002_auto_20170119_1630'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0004_message_context'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'get_latest_by': 'timestamp'},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='timestamp',
            new_name='created',
        ),
        migrations.AddField(
            model_name='room',
            name='accounts',
            field=models.ManyToManyField(related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_chatroom', to='classrooms.Classroom'),
        ),
        migrations.AddField(
            model_name='room',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='label',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
