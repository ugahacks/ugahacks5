# Generated by Django 2.2.10 on 2020-05-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_mlh_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_mentor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_sponsor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='on_duty',
            field=models.BooleanField(default=False),
        ),
    ]
