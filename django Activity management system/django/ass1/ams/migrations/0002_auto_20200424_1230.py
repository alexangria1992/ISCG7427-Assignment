# Generated by Django 3.0.5 on 2020-04-24 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=15)),
                ('enrolled_activities', models.ManyToManyField(blank=True, null=True, to='ams.Activity')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='myChildren',
            field=models.ManyToManyField(blank=True, null=True, to='ams.Child'),
        ),
    ]