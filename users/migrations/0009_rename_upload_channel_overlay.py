# Generated by Django 4.2 on 2023-06-11 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_channel_upload_alter_channel_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='upload',
            new_name='overlay',
        ),
    ]
