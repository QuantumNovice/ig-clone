# Generated by Django 4.0.4 on 2022-08-31 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to='<function user_directory_path at 0x0000013CDEE1D700>/% Y/% m/% d/')),
            ],
        ),
    ]
