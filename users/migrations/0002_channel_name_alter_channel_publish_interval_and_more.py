# Generated by Django 4.2 on 2023-05-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='name',
            field=models.CharField(default='Default', max_length=255),
        ),
        migrations.AlterField(
            model_name='channel',
            name='publish_interval',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='channel',
            name='themes',
            field=models.TextField(default=''),
        ),
    ]
