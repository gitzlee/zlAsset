# Generated by Django 2.1.5 on 2019-01-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operSystem', '0004_cert_os_host_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='syncdata',
            name='update_time',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
