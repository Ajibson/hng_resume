# Generated by Django 3.2.6 on 2021-08-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_refrence_id_resume_details_reference_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume_details',
            old_name='end_date',
            new_name='edu_end_date',
        ),
        migrations.RenameField(
            model_name='resume_details',
            old_name='start_date',
            new_name='edu_start_date',
        ),
        migrations.AddField(
            model_name='resume_details',
            name='work_end_date',
            field=models.CharField(default='2021-06-25', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_details',
            name='work_start_date',
            field=models.CharField(default='2021-06-25', max_length=30),
            preserve_default=False,
        ),
    ]
