# Generated by Django 5.0.3 on 2024-03-14 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_records', '0006_alter_patientrecord_client_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecord',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]