# Generated by Django 3.1.1 on 2020-09-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_auto_20200919_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveller',
            name='dob',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
    ]