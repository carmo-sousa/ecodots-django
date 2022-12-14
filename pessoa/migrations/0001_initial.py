# Generated by Django 4.1.3 on 2022-12-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf_cnpj', models.CharField(max_length=16, unique=True)),
                ('tipo', models.CharField(choices=[('F', 'Fisica'), ('J', 'Juridica')], default='F', max_length=1)),
            ],
        ),
    ]
