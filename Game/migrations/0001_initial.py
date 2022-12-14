# Generated by Django 4.1.2 on 2022-10-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_live', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
            ],
        ),
    ]
