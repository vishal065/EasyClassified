# Generated by Django 3.2.9 on 2021-12-05 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
