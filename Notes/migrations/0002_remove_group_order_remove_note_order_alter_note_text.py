# Generated by Django 5.0 on 2024-01-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='order',
        ),
        migrations.RemoveField(
            model_name='note',
            name='order',
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
