# Generated by Django 4.2.7 on 2023-11-24 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_complaint_type_of_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Type_of_complaint',
            field=models.CharField(choices=[('', '--Select Type of Complaint--'), ('Street Lights', 'Street Lights'), ('Water Pipe Leakage', 'Water Pipe Leakage'), ('Drainage', 'Drainage'), ('Roads', 'Roads'), ('Other', 'Other')], default='Type of complaint', max_length=200, null=True),
        ),
    ]
