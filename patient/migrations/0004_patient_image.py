# Generated by Django 5.1.6 on 2025-03-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='image',
            field=models.ImageField(blank='True', upload_to='patient_images/'),
        ),
    ]
