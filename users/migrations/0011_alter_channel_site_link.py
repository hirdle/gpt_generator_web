# Generated by Django 4.2 on 2023-07-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_channel_site_link_channel_vk_api_key_channel_vk_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='site_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
