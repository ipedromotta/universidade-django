# Generated by Django 3.2.7 on 2021-09-27 18:25

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alterado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 9, 27, 18, 25, 20, 764518, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='publicado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')], default='rascunho', max_length=10),
        ),
    ]
