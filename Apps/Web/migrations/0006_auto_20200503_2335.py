# Generated by Django 3.0.5 on 2020-05-03 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0005_delete_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='collection_center_id',
            new_name='collection_center',
        ),
    ]
