# Generated by Django 3.1.2 on 2020-12-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20201212_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invDate',
            field=models.DateField(),
        ),
    ]