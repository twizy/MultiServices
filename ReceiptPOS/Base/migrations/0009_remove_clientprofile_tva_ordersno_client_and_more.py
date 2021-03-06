# Generated by Django 4.0.4 on 2022-05-24 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0008_alter_ordersno_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='tva',
        ),
        migrations.AddField(
            model_name='ordersno',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Base.clientprofile', verbose_name='Client name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordersno',
            name='quantity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
