# Generated by Django 5.0.2 on 2024-02-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_registration_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
