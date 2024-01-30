# Generated by Django 5.0.1 on 2024-01-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reuniao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200)),
                ('local', models.CharField(max_length=100)),
                ('nome_participante', models.CharField(max_length=100)),
                ('dia', models.DateField()),
                ('horario', models.TimeField()),
            ],
        ),
    ]
