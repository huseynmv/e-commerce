# Generated by Django 4.0 on 2022-02-18 21:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='link',
        ),
        migrations.AddField(
            model_name='blog',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Content', null=True),
        ),
    ]