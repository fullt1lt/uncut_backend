from rest_framework import serializers
from myappback.models import CategoryActivity, Doctors, ProcedureActivity


class ProcedureActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureActivity
        fields = ['id','text_en', 'text_uk']
        
        
class CategoryActivitySerializer(serializers.ModelSerializer):
    procedures = ProcedureActivitySerializer(many=True)

    class Meta:
        model = CategoryActivity
        fields = ['id','title_en', 'title_uk', 'procedures']
        
        
class DoctorSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    image_info = serializers.ImageField(required=False)

    class Meta:
        model = Doctors
        fields = [
            'id', 'specialization_en', 'specialization_uk', 'name_en', 'name_uk', 'about_myself_en', 'about_myself_uk',
            'photo', 'information_en', 'information_uk', 'image_info', 'specialty_en', 'specialty_uk', 'education_en',
            'education_uk', 'experience_en', 'experience_uk', 'work_method_en', 'work_method_uk', 'work_directions_en',
            'work_directions_uk', 'skills_en', 'skills_uk', 'professional_development_en', 'professional_development_uk',
            'additional_professional_activity_en', 'additional_professional_activity_uk'
        ]