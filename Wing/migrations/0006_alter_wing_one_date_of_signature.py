# Generated by Django 5.1.1 on 2024-10-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wing', '0005_wing_one_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wing_one',
            name='date_of_signature',
            field=models.DateTimeField(),
        ),
    ]