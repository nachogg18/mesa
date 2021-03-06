# Generated by Django 3.2 on 2021-04-20 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0002_alter_consulta_estadoconsulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='apellidoSolitante',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='emailSolicitante',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='nombreSolicitante',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='solicitante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='entities.solicitante'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='tipoProblema',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='entities.tipoproblema'),
        ),
        migrations.AlterField(
            model_name='tiposolicitante',
            name='nombreTipoSolicitante',
            field=models.CharField(max_length=30),
        ),
    ]
