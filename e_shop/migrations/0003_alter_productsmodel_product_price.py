# Generated by Django 4.0.4 on 2022-05-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0002_alter_productsmodel_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='product_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
