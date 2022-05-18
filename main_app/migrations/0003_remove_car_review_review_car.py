# Generated by Django 4.0.3 on 2022-05-17 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_car_mileage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='car',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.car'),
            preserve_default=False,
        ),
    ]