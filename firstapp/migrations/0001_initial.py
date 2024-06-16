# Generated by Django 5.0.6 on 2024-06-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=200)),
                ('taskDescription', models.TextField(blank=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
