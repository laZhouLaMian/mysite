# Generated by Django 5.0.1 on 2024-04-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_options_alter_task_taskgroup_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
