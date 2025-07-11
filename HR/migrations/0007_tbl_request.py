# Generated by Django 5.1.7 on 2025-04-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0006_delete_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='applications/resumes/')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('request_status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0)),
            ],
        ),
    ]
