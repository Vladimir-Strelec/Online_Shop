# Generated by Django 5.0.3 on 2024-05-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_client_numer_shopuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
