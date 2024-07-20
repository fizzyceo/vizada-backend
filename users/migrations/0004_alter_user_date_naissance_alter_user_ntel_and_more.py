# Generated by Django 5.0.6 on 2024-06-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_date_naissance_alter_user_ntel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_naissance',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ntel',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.BooleanField(default=False, verbose_name='Role'),
        ),
    ]
