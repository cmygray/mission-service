# Generated by Django 2.2.2 on 2019-06-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190618_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='ends_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='starts_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
