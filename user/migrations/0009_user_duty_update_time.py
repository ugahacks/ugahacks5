# Generated by Django 2.2.13 on 2020-06-28 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200531_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='duty_update_time',
            field=models.DateTimeField(null=True, verbose_name='Last Checked In'),
        ),
    ]
