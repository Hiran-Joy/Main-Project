# Generated by Django 5.1.7 on 2025-04-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0003_tbl_recruitment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_recruitment',
            name='recruitment_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
