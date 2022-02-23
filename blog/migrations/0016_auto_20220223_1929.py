# Generated by Django 3.2.12 on 2022-02-23 19:29

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('blog', '0015_auto_20220223_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tag',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='BlogTag',
        ),
    ]
