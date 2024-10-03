# Generated by Django 5.0.7 on 2024-10-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappback', '0010_specialty_doctors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='specialty',
        ),
        migrations.AddField(
            model_name='doctors',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='name_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Specialty',
        ),
        migrations.AddField(
            model_name='doctors',
            name='specialty',
            field=models.CharField(default='Доктор', max_length=255),
        ),
    ]
