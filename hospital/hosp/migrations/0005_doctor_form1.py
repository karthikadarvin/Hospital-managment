# Generated by Django 4.2.7 on 2023-12-28 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp', '0004_admin_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_form1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=25)),
                ('doctor_id', models.CharField(max_length=25)),
                ('doctor_img', models.CharField(max_length=25)),
                ('doctor_dept', models.CharField(max_length=25)),
            ],
        ),
    ]
