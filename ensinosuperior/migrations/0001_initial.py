# Generated by Django 4.0.6 on 2024-04-08 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apresentacao', models.TextField(blank=True, null=True)),
                ('objetivos', models.TextField(blank=True, null=True)),
                ('competencias', models.TextField(blank=True, null=True)),
                ('horas_contacto_total', models.CharField(max_length=10)),
                ('ects', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ramo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('semestre', models.CharField(max_length=15)),
                ('ects', models.IntegerField()),
                ('horas_contacto', models.CharField(max_length=10)),
                ('curricularIUnitReadableCode', models.CharField(max_length=100)),
                ('area_cientifica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Disciplinas', to='ensinosuperior.areacientifica')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('conceitos_aplicados', models.TextField(blank=True, null=True)),
                ('link_video', models.URLField(null=True)),
                ('link_github', models.URLField(null=True)),
                ('disciplina', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projeto', to='ensinosuperior.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='LinguagemProgramacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('projetos', models.ManyToManyField(related_name='linguagem_programacao', to='ensinosuperior.projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, null=True)),
                ('disciplinas', models.ManyToManyField(related_name='docentes', to='ensinosuperior.disciplina')),
            ],
        ),
    ]
