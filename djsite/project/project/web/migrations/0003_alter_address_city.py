# Generated by Django 5.0.3 on 2024-03-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_order_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Nürnberg', 'Nürnberg'), ('Erlangen', 'Erlangen'), ('Fürth', 'Fürth'), ('Schvabach', 'Schvabach'), ('Roth', 'Roth')], default='Nürnberg', max_length=50),
        ),
    ]
