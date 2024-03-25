# Generated by Django 4.1.13 on 2024-01-22 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dtesv', '0014_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos',
            name='proveedor_id',
            field=models.ForeignKey(blank=True, db_column='proveedor_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='documento_proveedor_id', to='dtesv.proveedor'),
        ),
    ]