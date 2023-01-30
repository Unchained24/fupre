# Generated by Django 4.1.5 on 2023-01-30 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_alter_student_level'),
        ('courses', '0005_alter_registered_credit_unit'),
        ('configuration', '0010_department_number_of_years'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca', models.IntegerField()),
                ('exam', models.IntegerField()),
                ('lecturer', models.CharField(blank=True, max_length=200, null=True)),
                ('ref', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.semester')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
