# Generated by Django 2.2.2 on 2019-06-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190616_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='ends_at',
            field=models.DateTimeField(),
        ),
    ]
