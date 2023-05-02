# Generated by Django 4.2 on 2023-05-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menuitem_description_alter_menuitem_name_and_more'),
        ('users', '0002_alter_user_options_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favored_by', to='menu.menuitem'),
        ),
    ]
