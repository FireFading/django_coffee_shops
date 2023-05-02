# Generated by Django 4.2 on 2023-05-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number')),
                ('opening_time', models.TimeField(verbose_name='Opening time')),
                ('closing_time', models.TimeField(verbose_name='Closing time')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
                'ordering': ['-name'],
            },
        ),
    ]
