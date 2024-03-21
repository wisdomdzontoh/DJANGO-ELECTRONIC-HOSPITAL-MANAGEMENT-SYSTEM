# Generated by Django 5.0.3 on 2024-03-20 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conditions', '0001_initial'),
        ('nursestation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_diagnosis', models.DateField()),
                ('pregnant_patient', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('principal_diagnosis_status_of_diagnosis', models.CharField(choices=[('none', 'None'), ('new_case', 'New Case'), ('old_case', 'Old Case')], max_length=20)),
                ('additional_diagnosis_status_of_diagnosis', models.CharField(choices=[('none', 'None'), ('new_case', 'New Case'), ('old_case', 'Old Case')], max_length=20)),
                ('other_diagnosis', models.TextField()),
                ('other_diagnosis_status_of_diagnosis', models.CharField(choices=[('none', 'None'), ('new_case', 'New Case'), ('old_case', 'Old Case')], max_length=20)),
                ('additional_diagnosis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional_diagnoses', to='conditions.conditions')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nursestation.nursestation')),
                ('principal_diagnosis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='principal_diagnoses', to='conditions.conditions')),
                ('provisional_diagnosis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provisional_diagnoses', to='conditions.conditions')),
            ],
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_lab_request', models.CharField(choices=[('RDT', 'RDT'), ('microscopy', 'Microscopy'), ('Hep_B', 'Hep B')], max_length=10)),
                ('time_requested', models.DateTimeField(auto_now_add=True)),
                ('lab_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultingroom.consultingroom')),
            ],
        ),
    ]
