# Generated by Django 4.1.5 on 2023-01-09 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0002_alter_user_image_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='configuration.faculty'),
            preserve_default=False,
        ),
    ]
