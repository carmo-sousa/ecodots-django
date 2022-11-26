# Generated by Django 4.1.3 on 2022-11-24 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('C', 'Comercial'), ('P', 'Pessoal')], max_length=1)),
                ('telefone', models.CharField(blank=True, max_length=9, null=True)),
                ('dd', models.CharField(blank=True, max_length=3, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
            options={
                'ordering': ['cliente'],
            },
        ),
    ]
