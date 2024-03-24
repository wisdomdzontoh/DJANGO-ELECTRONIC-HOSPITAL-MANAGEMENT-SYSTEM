# Generated by Django 5.0.3 on 2024-03-23 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultingroom', '0002_consultingroom_clinical_notes_labtest_notes_and_more'),
        ('laboratory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultingroom',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='consultingroom',
            name='age_group',
            field=models.CharField(choices=[('0-28 days', '0-28 days'), ('1-11 months', '1-11 months'), ('1-4 years', '1-4 years'), ('5-9 years', '5-9 years'), ('10-14 years', '10-14 years'), ('15-17 years', '15-17 years'), ('18-19 years', '18-19 years'), ('20-34 years', '20-34 years'), ('35-49 years', '35-49 years'), ('50-59 years', '50-59 years'), ('60-69 years', '60-69 years'), ('70+ yrs & Above', '70 yrs & Above')], default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='consultingroom',
            name='age_type',
            field=models.CharField(choices=[('days', 'days'), ('months', 'months'), ('years', 'years')], default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='consultingroom',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='none', max_length=1),
        ),
        migrations.AlterField(
            model_name='labtest',
            name='type_of_lab_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.testtypes'),
        ),
    ]
