# Generated by Django 4.0.3 on 2022-03-12 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='math',
            name='opration',
            field=models.CharField(choices=[('add', 'add'), ('sub', 'sub'), ('mul', 'mul'), ('div', 'div')], max_length=5),
        ),
    ]
