# Generated by Django 4.0.4 on 2022-08-31 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_student_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]