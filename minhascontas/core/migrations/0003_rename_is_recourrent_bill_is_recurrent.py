# Generated by Django 3.2.5 on 2021-07-29 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bill_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='is_recourrent',
            new_name='is_recurrent',
        ),
    ]