# Generated by Django 5.1.6 on 2025-02-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(max_length=20)),
                ('doctor', models.CharField(max_length=30)),
                ('diagnosis', models.TextField(max_length=200)),
                ('date_diagnosed', models.DateField()),
            ],
        ),
    ]
