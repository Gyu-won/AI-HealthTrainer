# Generated by Django 4.2.4 on 2023-08-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AI_HealthTrainer', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='goal',
            name='start',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='goal',
            name='stop',
            field=models.DateField(),
        ),
    ]