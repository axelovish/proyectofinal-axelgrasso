# Generated by Django 4.0 on 2022-05-23 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0013_alter_comentario_comentario_alter_comentario_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='nombre',
            field=models.TextField(blank=True, null=True),
        ),
    ]