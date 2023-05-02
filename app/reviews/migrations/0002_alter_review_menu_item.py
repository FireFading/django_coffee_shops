# Generated by Django 4.2 on 2023-05-02 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menuitem_description_alter_menuitem_name_and_more'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='menu.menuitem', verbose_name='Menu Item'),
        ),
    ]
