# Generated by Django 3.0.6 on 2020-06-05 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Report_Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], max_length=1)),
                ('subject_name', models.CharField(max_length=30)),
                ('subject_marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Student')),
            ],
        ),
    ]