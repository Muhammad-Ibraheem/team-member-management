# Generated by Django 3.2.12 on 2023-11-28 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TeamMemberManagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='phone_numer',
            new_name='phone_number',
        ),
    ]
