# Generated by Django 2.2.6 on 2019-10-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_auto_20191026_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='max_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='min_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
