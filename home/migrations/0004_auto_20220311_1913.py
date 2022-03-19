# Generated by Django 3.2.12 on 2022-03-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homesecondaryslider'),
    ]

    operations = [
        migrations.AddField(
            model_name='homesecondaryslider',
            name='desc_az',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='homesecondaryslider',
            name='desc_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='homesecondaryslider',
            name='title_az',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='homesecondaryslider',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]