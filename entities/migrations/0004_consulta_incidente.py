# Generated by Django 3.2 on 2021-04-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0003_auto_20210420_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='incidente',
            field=models.IntegerField(null=True),
        ),
    ]