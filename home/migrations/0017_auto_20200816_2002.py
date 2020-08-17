# Generated by Django 3.0.5 on 2020-08-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20200812_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='comment_from_perm_sec1',
            new_name='comment_from_perm_sec_cas',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='comment_from_perm_sec2',
            new_name='comment_from_perm_sec_political',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='moved_to_perm_sec',
            new_name='moved_from_perm_sec_cas',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='perm_sec',
            new_name='perm_sec_cas',
        ),
        migrations.AddField(
            model_name='file',
            name='comment_from_director_cabinet_affairs',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='comment_from_director_internal_affairs',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='comment_from_director_security',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='comment_from_perm_sec_general_admin',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_from_director_cabinet_affairs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_from_director_internal_affairs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_from_director_security',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_from_perm_sec_general_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_from_perm_sec_political',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_from_ssg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_to_director_cabinet_affairs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_to_director_internal_affairs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_to_director_security',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_to_perm_sec_cas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_to_perm_sec_general_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='moved_to_ssg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='director_cabinet_affairs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='director_internal_affairs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='director_security',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='perm_sec_general_admin',
            field=models.BooleanField(default=False),
        ),
    ]