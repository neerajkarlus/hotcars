# Generated by Django 4.1.4 on 2023-03-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0041_alter_testdrive_dattte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdrive',
            name='dattte',
            field=models.DateTimeField(default=0, null=True, verbose_name='Customer Perfer Time For Test Drive'),
        ),
    ]