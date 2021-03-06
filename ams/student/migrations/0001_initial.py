# Generated by Django 2.0.1 on 2018-01-21 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('create', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=100, unique=True)),
                ('agn_file', models.FileField(upload_to='')),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create.create_assignment')),
            ],
        ),
    ]
