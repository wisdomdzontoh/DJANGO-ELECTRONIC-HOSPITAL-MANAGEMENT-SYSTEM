# Generated by Django 5.0.3 on 2024-03-21 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_test', models.CharField(max_length=250)),
                ('type_of_test', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('last_updated', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
