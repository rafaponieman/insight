# Generated by Django 4.2.6 on 2023-10-29 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='run start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='run end')),
                ('status', models.CharField(choices=[('queued', 'Queued'), ('in_progress', 'In progress'), ('completed', 'Completed'), ('failed', 'Failed')], default='queued', max_length=100, verbose_name='status')),
                ('logs', models.TextField(blank=True, verbose_name='logs')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seekers.seeker')),
            ],
            options={
                'verbose_name': 'training',
                'verbose_name_plural': 'trainings',
            },
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='run start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='run end')),
                ('status', models.CharField(choices=[('queued', 'Queued'), ('in_progress', 'In progress'), ('completed', 'Completed'), ('failed', 'Failed')], default='queued', max_length=100, verbose_name='status')),
                ('logs', models.TextField(blank=True, verbose_name='logs')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seekers.seeker')),
            ],
            options={
                'verbose_name': 'run',
                'verbose_name_plural': 'runs',
            },
        ),
    ]
