# Generated by Django 4.2.5 on 2023-09-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_subscribed_delete_subscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='mobile',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='number',
            field=models.IntegerField(max_length=100),
        ),
    ]
