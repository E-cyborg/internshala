# Generated by Django 5.2.3 on 2025-06-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aUTH', '0002_cuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='address_line1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='pincode',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='profile_picture',
            field=models.ImageField(upload_to='profiles/'),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='state',
            field=models.CharField(max_length=100),
        ),
    ]
