# Generated by Django 5.2.1 on 2025-05-28 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_order_stock_id_alter_order_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='stock_id',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
    ]
