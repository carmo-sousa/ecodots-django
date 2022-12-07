# Generated by Django 4.1.3 on 2022-12-05 21:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='dt_alteracao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data de alteração'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='dt_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de criação'),
        ),
    ]
