# Generated by Django 4.0.4 on 2022-05-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('products', '0001_initial'), ('products', '0002_alter_product_title'), ('products', '0003_alter_product_price'), ('products', '0004_product_description'), ('products', '0005_product_short_description'), ('products', '0006_remove_product_short_description')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
