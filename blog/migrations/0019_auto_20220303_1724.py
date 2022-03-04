# Generated by Django 3.2.12 on 2022-03-03 17:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='desc_az',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Content', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='desc_en',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Content', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_az',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_en',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]