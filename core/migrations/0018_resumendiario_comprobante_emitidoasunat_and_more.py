# Generated by Django 4.2.16 on 2024-11-13 14:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_entidad_celular_alter_entidad_numerodocumento'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumenDiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(max_length=4)),
                ('numeroResumen', models.CharField(max_length=8)),
                ('fechaEmision', models.DateField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comprobante',
            name='emitidoASunat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notacredito',
            name='emitidoASunat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notadebito',
            name='emitidoASunat',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='serie',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='resumenDeEmision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.resumendiario'),
        ),
        migrations.AddField(
            model_name='notacredito',
            name='resumenDeEmision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.resumendiario'),
        ),
        migrations.AddField(
            model_name='notadebito',
            name='resumenDeEmision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.resumendiario'),
        ),
    ]