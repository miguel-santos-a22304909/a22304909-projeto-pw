# Generated by Django 4.0.6 on 2024-04-23 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='praia',
            name='foto',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='capas'),
        ),
    ]
