# Generated by Django 2.2.13 on 2020-07-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_user_duty_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='static/images/stock_profile_picture.jpg', upload_to='profile_picture'),
        ),
    ]
