# Generated by Django 4.0.6 on 2024-04-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0003_rename_nome_album_titulo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='capa',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='capas'),
        ),
    ]
