# Generated by Django 5.1.2 on 2024-11-19 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('Numno', models.IntegerField(primary_key='Numno', serialize=False)),
                ('Adderes', models.CharField(max_length=30)),
                ('Aadhar', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
