# Generated by Django 4.2.2 on 2024-01-25 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_remove_conversation_media_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Conversation',
        ),
    ]
