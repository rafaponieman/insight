# Generated by Django 4.2.6 on 2023-10-30 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekers', '0003_run_name_seeker_prototype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='run',
            options={'ordering': ('-created',), 'verbose_name': 'run', 'verbose_name_plural': 'runs'},
        ),
        migrations.AlterField(
            model_name='run',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='run',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='training',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='training',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified')),
                ('timestamp', models.PositiveBigIntegerField(db_index=True, verbose_name='timestamp')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='seekers.run')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'ordering': ('timestamp',),
            },
        ),
    ]
