# Generated by Django 3.2.19 on 2023-05-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sangsi', '0002_alter_sangsi_audition_recruitment_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sangsi_audition',
            name='detail_data',
        ),
        migrations.AddField(
            model_name='sangsi_audition',
            name='data_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
