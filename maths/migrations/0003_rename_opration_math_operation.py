# Generated by Django 4.0.3 on 2022-03-12 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0002_alter_math_opration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='math',
            old_name='opration',
            new_name='operation',
        ),
    ]