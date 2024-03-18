# Generated by Django 5.0.3 on 2024-03-17 21:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient_records', '0007_alter_patientrecord_gender'),
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NurseStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_appointment', models.DateTimeField()),
                ('reason_of_appointment', models.TextField(default='none', max_length=255)),
                ('appointment_created_at', models.DateTimeField(auto_now_add=True)),
                ('SPO2', models.CharField(default='none', max_length=50)),
                ('respiratory_rate', models.CharField(default='none', max_length=50)),
                ('pulse', models.CharField(default='none', max_length=50)),
                ('RBS', models.CharField(default='none', max_length=50)),
                ('weight', models.CharField(default='none', max_length=50)),
                ('height', models.CharField(default='none', max_length=50)),
                ('BP', models.CharField(default='none', max_length=50)),
                ('temperature', models.CharField(default='none', max_length=50)),
                ('status_of_appointment', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_records.patientrecord')),
                ('type_of_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
    ]