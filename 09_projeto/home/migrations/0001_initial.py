# Generated by Django 5.0.1 on 2024-01-12 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_carne', models.CharField(max_length=100)),
                ('tipos_da_carne', models.CharField(max_length=100)),
                ('data_do_corte', models.IntegerField()),
                ('fazenda_que_vendeu_a_carne', models.CharField(max_length=100)),
                ('preco', models.FloatField(default=0.0)),
            ],
        ),
    ]
