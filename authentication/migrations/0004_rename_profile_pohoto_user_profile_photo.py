# Generated by Django 4.2.3 on 2023-08-18 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile_pohoto',
            new_name='profile_photo',
        ),
    ]