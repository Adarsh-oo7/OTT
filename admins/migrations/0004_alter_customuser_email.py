# Generated by Django 5.1.1 on 2024-10-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_alter_customuser_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
