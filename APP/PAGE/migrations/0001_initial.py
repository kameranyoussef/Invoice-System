# Generated by Django 4.1.7 on 2023-06-16 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("contact", models.CharField(max_length=100)),
                ("tel", models.DecimalField(decimal_places=0, max_digits=16)),
                ("email", models.EmailField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("plz", models.IntegerField()),
                ("ort", models.CharField(max_length=100)),
                ("land", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Company",
                "verbose_name_plural": "Companies",
                "default_related_name": "Company",
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("tel", models.DecimalField(decimal_places=0, max_digits=16)),
                ("email", models.EmailField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("plz", models.IntegerField()),
                ("ort", models.CharField(max_length=100)),
                ("land", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Customer",
                "verbose_name_plural": "Customers",
                "default_related_name": "Customer",
            },
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "company",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="PAGE.company",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="PAGE.customer",
                    ),
                ),
            ],
            options={
                "verbose_name": "Invoice",
                "verbose_name_plural": "Invoices",
                "default_related_name": "Invoice",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("product", models.CharField(max_length=100)),
                ("unit", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("count", models.IntegerField()),
                ("vat", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="PAGE.invoice"
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "default_related_name": "Product",
            },
        ),
    ]