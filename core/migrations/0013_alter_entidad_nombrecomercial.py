# Generated by Django 4.2.16 on 2024-10-25 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_estadodocumento_comprobante_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='nombreComercial',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
