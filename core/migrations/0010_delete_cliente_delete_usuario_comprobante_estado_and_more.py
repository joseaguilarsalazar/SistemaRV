# Generated by Django 4.2.16 on 2024-10-24 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_catalogo51tipodeoperacion_codigo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='comprobante',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.estadodocumento'),
        ),
        migrations.AlterField(
            model_name='estadodocumento',
            name='nombre',
            field=models.CharField(db_column='nombre', max_length=50, null=True),
        ),
    ]
