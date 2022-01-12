# Generated by Django 4.0 on 2021-12-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
