# Generated by Django 4.0.6 on 2024-03-12 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('capa', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='')),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao_segundos', models.IntegerField(verbose_name='Duração em segundos')),
                ('link_spotify', models.URLField(null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.album')),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.banda')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albuns', to='bandas.banda'),
        ),
    ]
