# Generated by Django 3.2.12 on 2022-02-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20220221_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]
