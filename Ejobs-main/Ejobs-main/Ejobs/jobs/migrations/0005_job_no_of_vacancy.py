# Generated by Django 3.2 on 2021-04-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_job_job_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='no_of_vacancy',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
