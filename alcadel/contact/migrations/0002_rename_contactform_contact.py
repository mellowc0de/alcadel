# Generated by Django 3.2.8 on 2021-10-12 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contactForm',
            new_name='Contact',
        ),
    ]