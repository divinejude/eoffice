# Generated by Django 3.0.5 on 2020-08-12 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200812_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='moved_to_sec',
            new_name='moved_to_perm_sec',
        ),
    ]
