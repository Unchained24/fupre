# Generated by Django 4.1.5 on 2023-01-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_department_setup'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered',
            name='credit_unit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
