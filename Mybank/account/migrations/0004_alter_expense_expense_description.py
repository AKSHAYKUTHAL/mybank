# Generated by Django 4.2.4 on 2023-09-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_amount_expense_expense_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_description',
            field=models.TextField(),
        ),
    ]