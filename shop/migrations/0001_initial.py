# Generated by Django 4.0 on 2022-02-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=127, null=True)),
                ('name', models.CharField(blank=True, max_length=127, null=True)),
                ('price', models.SmallIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(upload_to='shop/')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
