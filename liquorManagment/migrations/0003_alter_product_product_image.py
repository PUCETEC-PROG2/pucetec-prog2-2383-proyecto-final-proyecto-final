# Generated by Django 4.2 on 2024-08-14 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liquorManagment', '0002_purchase_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='product_images/'),
        ),
    ]
