# Generated by Django 4.1.7 on 2023-04-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WasteContainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont_type', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('cont_type',),
            },
        ),
        migrations.CreateModel(
            name='Waste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_name', models.CharField(max_length=150)),
                ('type', models.ManyToManyField(to='waste_sorting.wastecontainer')),
            ],
            options={
                'ordering': ('waste_name',),
            },
        ),
    ]
