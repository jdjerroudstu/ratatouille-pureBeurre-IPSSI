# Generated by Django 4.1.5 on 2023-01-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangobackend", "0004_products_delete_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="subtituteProduct",
            fields=[
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("product_name", models.CharField(max_length=200)),
                ("categories", models.CharField(max_length=200)),
                ("brands", models.CharField(max_length=200)),
                ("stores", models.CharField(max_length=200)),
                ("url", models.CharField(max_length=300)),
            ],
        ),
        migrations.RenameModel(
            old_name="Products",
            new_name="Product",
        ),
    ]
