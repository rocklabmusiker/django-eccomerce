# Generated by Django 4.1.5 on 2023-01-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('New', 'New'), ('Feature', 'Feature'), ('Sale', 'Sales')], max_length=20, verbose_name='flag'),
        ),
    ]