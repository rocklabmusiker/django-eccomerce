# Generated by Django 4.1.5 on 2023-02-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('New', 'New'), ('Sale', 'Sales'), ('Feature', 'Feature')], max_length=20, verbose_name='flag'),
        ),
    ]