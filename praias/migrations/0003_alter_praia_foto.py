# Generated by Django 4.0.6 on 2024-04-23 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praias', '0002_praia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praia',
            name='foto',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='praias'),
        ),
    ]
