# Generated by Django 3.1.2 on 2020-11-27 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_manager', '0003_auto_20201113_0646'),
        ('payment_module', '0002_invoice_invoicedetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvoiceDetails',
            new_name='InvoiceDetail',
        ),
    ]