# Generated by Django 5.1.3 on 2024-11-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ELEARNING', '0003_alter_upload_passport_alter_upload_photo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='passport',
            field=models.ImageField(upload_to='document/'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='photo_id',
            field=models.ImageField(upload_to='document/'),
        ),
    ]
