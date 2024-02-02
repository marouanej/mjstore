# Generated by Django 4.2.2 on 2023-11-21 16:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_cuser_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuser',
            name='followers',
            field=models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]