# Generated by Django 3.2.6 on 2021-08-19 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_message_date_recieved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='message_recieved',
        ),
    ]
