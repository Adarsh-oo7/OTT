# Generated by Django 5.1.1 on 2024-10-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='token',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
