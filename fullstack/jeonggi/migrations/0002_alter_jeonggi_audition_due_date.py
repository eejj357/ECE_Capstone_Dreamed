# Generated by Django 3.2.19 on 2023-05-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeonggi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeonggi_audition',
            name='due_date',
            field=models.DateField(),
        ),
    ]
