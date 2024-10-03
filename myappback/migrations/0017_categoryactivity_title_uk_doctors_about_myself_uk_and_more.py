# Generated by Django 5.0.7 on 2024-10-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappback', '0016_remove_categoryactivity_title_uk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryactivity',
            name='title_uk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='about_myself_uk',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='additional_professional_activity_uk',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='education_uk',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='experience_uk',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='information_uk',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='name_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='professional_development_uk',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='skills_uk',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='specialization_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='specialty_uk',
            field=models.TextField(default='Доктор', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='work_directions_uk',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='work_method_uk',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='procedureactivity',
            name='text_uk',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
