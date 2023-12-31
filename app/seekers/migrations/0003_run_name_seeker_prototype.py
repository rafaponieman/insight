# Generated by Django 4.2.6 on 2023-10-30 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekers', '0002_training_run'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='name',
            field=models.CharField(blank=True, max_length=150, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='seeker',
            name='prototype',
            field=models.CharField(choices=[('test', 'Test')], default='test', help_text='This seeker instance will be based on the selected Prototype', max_length=100, verbose_name='prototype'),
            preserve_default=False,
        ),
    ]
