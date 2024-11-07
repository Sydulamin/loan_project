# Generated by Django 5.1.1 on 2024-10-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wing', '0004_wing_one_co_financer'),
    ]

    operations = [
        migrations.AddField(
            model_name='wing_one',
            name='status',
            field=models.CharField(choices=[('Highly Probable', 'Highly Probable'), ('Probable', 'Probable'), ('Signed', 'Signed')], default='Signed', max_length=100),
            preserve_default=False,
        ),
    ]