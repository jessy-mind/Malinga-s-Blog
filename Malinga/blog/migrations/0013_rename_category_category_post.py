# Generated by Django 4.2.4 on 2023-08-30 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_post_categories_category_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='post',
        ),
    ]