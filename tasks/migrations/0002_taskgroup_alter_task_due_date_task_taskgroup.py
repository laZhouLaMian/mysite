# Generated by Django 5.0.1 on 2024-02-19 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='taskgroup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.taskgroup'),
            preserve_default=False,
        ),
    ]
