# Generated by Django 5.0.6 on 2024-05-22 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0004_rename_newbalancedst_paymentdetails_newbalancedest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='oldBalanceOrig',
            new_name='oldBalanceOrg',
        ),
    ]