# Generated by Django 4.2 on 2023-05-03 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Comment to order')),
                ('total_price', models.FloatField(default=0, verbose_name='Total price')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated time')),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('PENDED', 'Pended'), ('COMPLETED', 'Completed')], default='CREATED', max_length=10, verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ('-created_time',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255, verbose_name='Product in order')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Product in order',
                'verbose_name_plural': 'Products in order',
            },
        ),
    ]
