# Generated by Django 4.0.4 on 2022-05-06 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_squashed_0006_remove_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='state',
            field=models.CharField(default='DR', max_length=2),
        ),
    ]
