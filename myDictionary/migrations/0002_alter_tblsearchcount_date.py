# Generated by Django 4.0.4 on 2022-06-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDictionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblsearchcount',
            name='date',
            field=models.DateField(),
        ),
    ]
