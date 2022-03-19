# Generated by Django 3.2.12 on 2022-03-19 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20220319_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='discount_percent',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='product',
            field=models.ForeignKey(blank=True, max_length=127, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='shop.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, max_length=127, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='shop.productcategory'),
        ),
    ]
