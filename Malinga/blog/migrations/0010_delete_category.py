# Generated by Django 4.2.4 on 2023-08-30 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_category_category_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]