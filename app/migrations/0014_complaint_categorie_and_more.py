# Generated by Django 4.2.7 on 2023-11-28 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_complaint_type_of_complaint_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint_Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Add_Category', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='complaint',
            name='Type_of_complaint',
            field=models.ForeignKey(default='Type of complaint', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.complaint_categorie'),
        ),
    ]