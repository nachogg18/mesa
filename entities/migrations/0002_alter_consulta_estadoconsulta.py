# Generated by Django 3.2 on 2021-04-19 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='estadoConsulta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='entities.estadoconsulta'),
        ),
    ]
