# Generated by Django 4.2.6 on 2023-10-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekers', '0004_alter_run_options_alter_run_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='from_timestamp',
            field=models.BigIntegerField(default=1698692799),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='run',
            name='to_timestamp',
            field=models.BigIntegerField(default=1698692799),
            preserve_default=False,
        ),
    ]
