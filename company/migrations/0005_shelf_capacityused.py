# Generated by Django 3.1.2 on 2020-12-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20201213_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelf',
            name='capacityUsed',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
