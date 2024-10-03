# Generated by Django 5.0.7 on 2024-10-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappback', '0013_remove_doctors_image_info_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='about_myself',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='about_myself_en',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='about_myself_uk',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='additional_professional_activity',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='additional_professional_activity_en',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='additional_professional_activity_uk',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='education',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='education_en',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='education_uk',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='experience',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='experience_en',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='experience_uk',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='information',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='information_en',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='information_uk',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='name_en',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='name_uk',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='professional_development',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='professional_development_en',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='professional_development_uk',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='skills',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='skills_en',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='skills_uk',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='specialization',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='specialization_en',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='specialization_uk',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='specialty',
            field=models.TextField(default='Доктор', max_length=255),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='specialty_en',
            field=models.TextField(default='Доктор', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='specialty_uk',
            field=models.TextField(default='Доктор', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='work_directions',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='work_directions_en',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='work_directions_uk',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='work_method',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='work_method_en',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='work_method_uk',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
