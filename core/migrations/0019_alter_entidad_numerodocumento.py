# Generated by Django 4.2.16 on 2024-11-04 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_entidad_numerodocumento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='numeroDocumento',
            field=models.CharField(max_length=11),
        ),
    ]
