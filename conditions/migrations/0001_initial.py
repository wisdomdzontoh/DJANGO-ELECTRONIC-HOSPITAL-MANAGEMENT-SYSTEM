# Generated by Django 5.0.3 on 2024-03-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_condition', models.CharField(max_length=50)),
                ('ICD11_code', models.CharField(max_length=50)),
                ('last_updated', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
