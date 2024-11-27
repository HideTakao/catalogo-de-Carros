# Generated by Django 4.2.16 on 2024-11-26 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_brand_alter_car_model_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(default=' ', upload_to='cars/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]